import assert from 'node:assert/strict';
import test from 'node:test';
import { onRequestPost as postEvent } from '../functions/api/events.js';
import { onRequestPost as postLead } from '../functions/api/leads.js';

class Statement {
  constructor(db, sql) { this.db = db; this.sql = sql; }
  bind(...values) { this.values = values; return this; }
  async run() { return this.db.execute(this); }
  async first() { return this.db.first(this); }
}

class MemoryD1 {
  constructor() { this.events = new Map(); this.leads = new Map(); }
  prepare(sql) { return new Statement(this, sql); }
  execute(statement) {
    const isLead = statement.sql.includes('INTO leads');
    const store = isLead ? this.leads : this.events;
    const id = statement.values[0];
    if (isLead && statement.sql.includes('WHERE NOT EXISTS') && this.events.has(statement.values[13])) {
      return { meta: { changes: 0 } };
    }
    if (!isLead && statement.values[17]) {
      const lead = this.leads.get(statement.values[17]);
      if (!lead || lead[1] !== statement.values[19]) return { meta: { changes: 0 } };
    }
    if (store.has(id)) return { meta: { changes: 0 } };
    store.set(id, statement.values);
    return { meta: { changes: 1 } };
  }
  async batch(statements) {
    const snapshots = [new Map(this.leads), new Map(this.events)];
    try { return statements.map((statement) => this.execute(statement)); }
    catch (error) { [this.leads, this.events] = snapshots; throw error; }
  }
  first(statement) {
    const lead = this.leads.get(statement.values[0]);
    if (!lead) return null;
    return {
      lead_event_id: lead[1], email: lead[2], design_id: lead[3], submitted_at: lead[4],
      experiment_id: lead[6], brand_id: lead[7], session_id: lead[8], anonymous_visitor_id: lead[9],
      cta_id: lead[10], form_id: lead[11], attribution_json: lead[12],
    };
  }
}

const attribution = {
  creative_id: 'CR_TEST_A',
  utm_source: 'meta',
  utm_medium: 'paid-social',
  utm_campaign: 'mvv-test',
  utm_content: 'creative-a',
  utm_term: 'antiques',
  fbclid: 'fb-test',
  meta_campaign_id: 'mc-1',
  meta_adset_id: 'mas-1',
  meta_ad_id: 'ma-1',
};

function common(overrides = {}) {
  return {
    event_id: 'evt_00000000-0000-4000-8000-000000000001',
    event_timestamp: '2026-08-19T12:00:00.000Z',
    event_schema_version: '0.1',
    experiment_id: 'mvv-r012-001',
    brand_id: 'worth-the-detour',
    session_id: 'ses_00000000-0000-4000-8000-000000000001',
    anonymous_visitor_id: 'av_00000000-0000-4000-8000-000000000001',
    page_url: 'https://worth-the-detour.com/',
    page_path: '/',
    referrer: null,
    device_type: 'desktop',
    viewport_width: 1440,
    viewport_height: 900,
    ...overrides,
  };
}

function request(path, body) {
  return new Request(`https://worth-the-detour.com${path}`, {
    method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify(body),
  });
}

test('accepts an event and suppresses the same event_id', async () => {
  const db = new MemoryD1();
  const body = { ...common(), event_name: 'landing_view', ...attribution };
  let response = await postEvent({ request: request('/api/events', body), env: { DB: db } });
  assert.equal(response.status, 202);
  assert.equal((await response.json()).duplicate, false);
  response = await postEvent({ request: request('/api/events', body), env: { DB: db } });
  assert.equal((await response.json()).duplicate, true);
  assert.equal(db.events.size, 1);
});

test('rejects unknown events, unexpected fields, and PII', async () => {
  const db = new MemoryD1();
  for (const body of [
    { ...common(), event_name: 'purchase' },
    { ...common(), event_name: 'landing_view', surprise: true },
    { ...common(), event_name: 'landing_view', email: 'person@example.com' },
    { ...common(), event_name: 'landing_view', page_url: 'https://example.com/?email=hidden' },
  ]) {
    const response = await postEvent({ request: request('/api/events', body), env: { DB: db } });
    assert.equal(response.status, 400);
  }
  assert.equal(db.events.size, 0);
});

test('stores a mismatched acquisition creative and selected design without PII in the event', async () => {
  const db = new MemoryD1();
  const body = {
    ...common(), ...attribution,
    lead_id: 'lead_00000000-0000-4000-8000-000000000001',
    email: '  Person@Example.COM ',
    design_id: 'Type-Led-4',
    cta_id: 'design-interest',
    form_id: 'availability-interest',
  };
  const response = await postLead({ request: request('/api/leads', body), env: { DB: db } });
  assert.equal(response.status, 201);
  assert.equal(db.leads.size, 1);
  assert.equal(db.events.size, 1);
  const lead = [...db.leads.values()][0];
  const event = [...db.events.values()][0];
  assert.equal(lead[2], 'person@example.com');
  assert.equal(lead[3], 'Type-Led-4');
  assert.equal(JSON.parse(lead[12]).creative_id, 'CR_TEST_A');
  assert.equal(JSON.parse(lead[12]).meta_ad_id, 'ma-1');
  assert.equal(event[1], 'lead_submit');
  assert.equal(JSON.parse(event[16]).design_id, 'Type-Led-4');
  assert.equal(JSON.parse(event[15]).creative_id, 'CR_TEST_A');
  assert.ok(!JSON.stringify(event).includes('person@example.com'));
});

test('rejects invalid leads and does not create a lead_submit event', async () => {
  const db = new MemoryD1();
  const base = { ...common(), lead_id: 'lead_valid', cta_id: 'design-interest', form_id: 'availability-interest' };
  for (const body of [
    { ...base, email: 'not-an-email', design_id: 'B2' },
    { ...base, email: 'person@example.com', design_id: 'Fashion-1D-GN' },
  ]) {
    const response = await postLead({ request: request('/api/leads', body), env: { DB: db } });
    assert.equal(response.status, 400);
  }
  assert.equal(db.leads.size, 0);
  assert.equal(db.events.size, 0);
});

test('preserves missing attribution as null and makes lead retries idempotent', async () => {
  const db = new MemoryD1();
  const body = {
    ...common(), lead_id: 'lead_retry', email: 'person@example.com', design_id: 'B2',
    cta_id: 'design-interest', form_id: 'availability-interest',
  };
  await postLead({ request: request('/api/leads', body), env: { DB: db } });
  const response = await postLead({ request: request('/api/leads', body), env: { DB: db } });
  assert.equal((await response.json()).duplicate, true);
  assert.equal(db.leads.size, 1);
  assert.equal(db.events.size, 1);
  const conflictingRetry = { ...body, event_id: 'evt_conflicting_retry' };
  const conflictResponse = await postLead({ request: request('/api/leads', conflictingRetry), env: { DB: db } });
  assert.equal(conflictResponse.status, 409);
  assert.equal(db.events.size, 1);
  const savedAttribution = JSON.parse([...db.leads.values()][0][12]);
  assert.equal(savedAttribution.creative_id, null);
  assert.equal(savedAttribution.meta_ad_id, null);
});

test('rejects a reused lead_id whose accepted submission content differs', async () => {
  const db = new MemoryD1();
  const body = {
    ...common(), lead_id: 'lead_collision', email: 'first@example.com', design_id: 'B2',
    cta_id: 'design-interest', form_id: 'availability-interest',
  };
  await postLead({ request: request('/api/leads', body), env: { DB: db } });
  const response = await postLead({
    request: request('/api/leads', { ...body, email: 'other@example.com' }), env: { DB: db },
  });
  assert.equal(response.status, 409);
  assert.equal([...db.leads.values()][0][2], 'first@example.com');
  assert.equal(db.events.size, 1);
});

test('rejects a lead whose event_id already belongs to another event', async () => {
  const db = new MemoryD1();
  const eventId = 'evt_cross_endpoint_collision';
  const eventResponse = await postEvent({
    request: request('/api/events', { ...common({ event_id: eventId }), event_name: 'landing_view' }),
    env: { DB: db },
  });
  assert.equal(eventResponse.status, 202);

  const response = await postLead({
    request: request('/api/leads', {
      ...common({ event_id: eventId }),
      lead_id: 'lead_cross_endpoint_collision',
      email: 'person@example.com',
      design_id: 'B2',
      cta_id: 'design-interest',
      form_id: 'availability-interest',
    }),
    env: { DB: db },
  });
  assert.equal(response.status, 409);
  assert.deepEqual(await response.json(), { ok: false, error: 'submission_conflict' });
  assert.equal(db.leads.size, 0);
  assert.equal(db.events.size, 1);
  assert.equal([...db.events.values()][0][1], 'landing_view');
});

test('returns failure when DB is unavailable', async () => {
  const response = await postLead({ request: request('/api/leads', {}), env: {} });
  assert.equal(response.status, 503);
  assert.equal((await response.json()).ok, false);
});
