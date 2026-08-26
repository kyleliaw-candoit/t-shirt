export const DESIGN_IDS = [
  'B2', 'A1', 'A3', 'YIF-M', 'YIF-F', 'C2', 'C3B', 'Fashion-1D-F', 'Type-Led-3', 'Type-Led-4',
];

export const ATTRIBUTION_FIELDS = [
  'creative_territory_id', 'creative_id', 'variant_id', 'utm_source', 'utm_medium',
  'utm_campaign', 'utm_content', 'utm_term', 'fbclid', 'meta_campaign_id',
  'meta_adset_id', 'meta_ad_id',
];

const EVENT_NAMES = ['landing_view', 'design_view', 'design_engagement', 'intent_click', 'lead_submit', 'page_exit'];
const COMMON_FIELDS = [
  'event_name', 'event_id', 'event_timestamp', 'event_schema_version', 'experiment_id', 'brand_id',
  'session_id', 'anonymous_visitor_id', 'page_url', 'page_path', 'referrer', 'device_type',
  'viewport_width', 'viewport_height', ...ATTRIBUTION_FIELDS,
];
const EVENT_FIELDS = {
  landing_view: ['landing_variant_id'],
  design_view: ['design_id', 'design_position', 'view_duration_ms'],
  design_engagement: ['design_id', 'interaction_type'],
  intent_click: ['design_id', 'cta_id', 'cta_location'],
  lead_submit: ['design_id', 'cta_id', 'form_id'],
  page_exit: ['session_duration_ms', 'max_scroll_depth', 'designs_viewed_count', 'first_meaningful_engagement_ms'],
};
const ID_PATTERN = /^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$/;
const EMAIL_PATTERN = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const EMAIL_LIKE_PATTERN = /[^\s@]+@[^\s@]+\.[^\s@]+/;

export function json(status, body) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-store' },
  });
}

export async function readJson(request) {
  if (request.method !== 'POST') throw validationError(405, 'method_not_allowed');
  if (!(request.headers.get('content-type') || '').toLowerCase().startsWith('application/json')) {
    throw validationError(415, 'unsupported_media_type');
  }
  const length = Number(request.headers.get('content-length') || 0);
  if (length > 16_384) throw validationError(413, 'request_too_large');
  const text = await request.text();
  if (text.length > 16_384) throw validationError(413, 'request_too_large');
  let value;
  try { value = JSON.parse(text); } catch { throw validationError(400, 'invalid_json'); }
  if (!value || typeof value !== 'object' || Array.isArray(value)) throw validationError(400, 'invalid_request');
  return value;
}

export function validationError(status, code) {
  return Object.assign(new Error(code), { status, code });
}

function requireString(value, field, max = 256, pattern) {
  if (typeof value !== 'string' || value.length < 1 || value.length > max || (pattern && !pattern.test(value))) {
    throw validationError(400, `invalid_${field}`);
  }
  return value;
}

function optionalString(value, field, max = 256) {
  if (value === undefined || value === null) return null;
  return requireString(value, field, max);
}

function integer(value, field, min, max) {
  if (!Number.isInteger(value) || value < min || value > max) throw validationError(400, `invalid_${field}`);
  return value;
}

function assertAllowedFields(value, allowed) {
  const unexpected = Object.keys(value).find((key) => !allowed.includes(key));
  if (unexpected) throw validationError(400, 'unexpected_field');
}

function assertNoPii(value) {
  const serialized = JSON.stringify(value);
  if (/"(?:email|name|first_name|last_name)"\s*:/i.test(serialized) || EMAIL_LIKE_PATTERN.test(serialized)) {
    throw validationError(400, 'pii_not_allowed');
  }
}

function validateCleanUrl(value, field, { absolute = true } = {}) {
  const raw = requireString(value, field, absolute ? 2048 : 1024);
  if (raw.includes('?') || raw.includes('#')) throw validationError(400, `invalid_${field}`);
  if (absolute) {
    let parsed;
    try { parsed = new URL(raw); } catch { throw validationError(400, `invalid_${field}`); }
    if (!['http:', 'https:'].includes(parsed.protocol) || parsed.username || parsed.password) {
      throw validationError(400, `invalid_${field}`);
    }
  } else if (!raw.startsWith('/')) {
    throw validationError(400, `invalid_${field}`);
  }
  return raw;
}

export function validateEvent(value, { allowLeadSubmit = false } = {}) {
  assertNoPii(value);
  const eventName = requireString(value.event_name, 'event_name', 32);
  if (!EVENT_NAMES.includes(eventName) || (eventName === 'lead_submit' && !allowLeadSubmit)) {
    throw validationError(400, 'invalid_event_name');
  }
  assertAllowedFields(value, [...COMMON_FIELDS, ...EVENT_FIELDS[eventName]]);
  requireString(value.event_id, 'event_id', 128, ID_PATTERN);
  const timestamp = requireString(value.event_timestamp, 'event_timestamp', 35);
  if (!Number.isFinite(Date.parse(timestamp))) throw validationError(400, 'invalid_event_timestamp');
  if (value.event_schema_version !== '0.1' || value.experiment_id !== 'mvv-r012-001' || value.brand_id !== 'worth-the-detour') {
    throw validationError(400, 'invalid_experiment_context');
  }
  requireString(value.session_id, 'session_id', 128, ID_PATTERN);
  requireString(value.anonymous_visitor_id, 'anonymous_visitor_id', 128, ID_PATTERN);
  validateCleanUrl(value.page_url, 'page_url');
  validateCleanUrl(value.page_path, 'page_path', { absolute: false });
  if (value.referrer !== undefined && value.referrer !== null) validateCleanUrl(value.referrer, 'referrer');
  if (!['mobile', 'tablet', 'desktop'].includes(value.device_type)) throw validationError(400, 'invalid_device_type');
  integer(value.viewport_width, 'viewport_width', 1, 20_000);
  integer(value.viewport_height, 'viewport_height', 1, 20_000);
  for (const field of ATTRIBUTION_FIELDS) optionalString(value[field], field, field === 'fbclid' ? 512 : 256);

  if (['design_view', 'design_engagement', 'intent_click', 'lead_submit'].includes(eventName)) {
    if (!DESIGN_IDS.includes(value.design_id)) throw validationError(400, 'invalid_design_id');
  }
  if (eventName === 'landing_view') optionalString(value.landing_variant_id, 'landing_variant_id', 128);
  if (eventName === 'design_view') {
    integer(value.design_position, 'design_position', 1, DESIGN_IDS.length);
    integer(value.view_duration_ms, 'view_duration_ms', 1000, 3_600_000);
  }
  if (eventName === 'design_engagement' && !['tap', 'image_expand', 'hover'].includes(value.interaction_type)) {
    throw validationError(400, 'invalid_interaction_type');
  }
  if (eventName === 'intent_click') {
    requireString(value.cta_id, 'cta_id', 128, ID_PATTERN);
    if (!['design_card'].includes(value.cta_location)) throw validationError(400, 'invalid_cta_location');
  }
  if (eventName === 'lead_submit') {
    requireString(value.cta_id, 'cta_id', 128, ID_PATTERN);
    requireString(value.form_id, 'form_id', 128, ID_PATTERN);
  }
  if (eventName === 'page_exit') {
    integer(value.session_duration_ms, 'session_duration_ms', 0, 86_400_000);
    integer(value.max_scroll_depth, 'max_scroll_depth', 0, 100);
    integer(value.designs_viewed_count, 'designs_viewed_count', 0, DESIGN_IDS.length);
    if (value.first_meaningful_engagement_ms !== null) {
      integer(value.first_meaningful_engagement_ms, 'first_meaningful_engagement_ms', 0, 86_400_000);
    }
  }
  return value;
}

export function validateLead(value) {
  const allowed = [
    'lead_id', 'email', 'design_id', 'event_id', 'event_timestamp', 'event_schema_version',
    'experiment_id', 'brand_id', 'session_id', 'anonymous_visitor_id', 'page_url', 'page_path',
    'referrer', 'device_type', 'viewport_width', 'viewport_height', 'cta_id', 'form_id', ...ATTRIBUTION_FIELDS,
  ];
  assertAllowedFields(value, allowed);
  requireString(value.lead_id, 'lead_id', 128, ID_PATTERN);
  const email = requireString(value.email, 'email', 254).trim().toLowerCase();
  if (!EMAIL_PATTERN.test(email)) throw validationError(400, 'invalid_email');
  if (!DESIGN_IDS.includes(value.design_id)) throw validationError(400, 'invalid_design_id');
  const { email: discardedEmail, lead_id: discardedLeadId, ...eventFields } = value;
  const event = validateEvent({ ...eventFields, event_name: 'lead_submit' }, { allowLeadSubmit: true });
  return { ...value, ...event, email };
}

export function eventStatement(db, event, receivedAt, requiredLeadId = null) {
  const properties = Object.fromEntries(EVENT_FIELDS[event.event_name].map((key) => [key, event[key] ?? null]));
  const attribution = Object.fromEntries(ATTRIBUTION_FIELDS.map((key) => [key, event[key] ?? null]));
  return db.prepare(`INSERT OR IGNORE INTO events (
    event_id, event_name, event_timestamp, server_received_at, event_schema_version, experiment_id, brand_id,
    session_id, anonymous_visitor_id, page_url, page_path, referrer, device_type, viewport_width, viewport_height,
    attribution_json, properties_json
  ) SELECT ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
    WHERE ? IS NULL OR EXISTS (
      SELECT 1 FROM leads WHERE lead_id = ? AND lead_event_id = ?
    )`)
    .bind(event.event_id, event.event_name, event.event_timestamp, receivedAt, event.event_schema_version,
      event.experiment_id, event.brand_id, event.session_id, event.anonymous_visitor_id, event.page_url,
      event.page_path, event.referrer ?? null, event.device_type, event.viewport_width, event.viewport_height,
      JSON.stringify(attribution), JSON.stringify(properties), requiredLeadId, requiredLeadId, event.event_id);
}

export function handleError(error) {
  if (error && error.status) return json(error.status, { ok: false, error: error.code });
  return json(500, { ok: false, error: 'service_unavailable' });
}
