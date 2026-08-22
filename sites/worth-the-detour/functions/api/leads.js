import {
  ATTRIBUTION_FIELDS, eventStatement, handleError, json, readJson, validateLead,
} from '../_shared/server.js';

export async function onRequestPost(context) {
  try {
    if (!context.env.DB) return json(503, { ok: false, error: 'service_unavailable' });
    const lead = validateLead(await readJson(context.request));
    const receivedAt = new Date().toISOString();
    const attribution = Object.fromEntries(ATTRIBUTION_FIELDS.map((key) => [key, lead[key] ?? null]));
    const leadStatement = context.env.DB.prepare(`INSERT OR IGNORE INTO leads (
      lead_id, lead_event_id, email, design_id, submitted_at, server_received_at, experiment_id, brand_id, session_id,
      anonymous_visitor_id, cta_id, form_id, attribution_json
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`)
      .bind(lead.lead_id, lead.event_id, lead.email, lead.design_id, lead.event_timestamp, receivedAt, lead.experiment_id,
        lead.brand_id, lead.session_id, lead.anonymous_visitor_id, lead.cta_id, lead.form_id,
        JSON.stringify(attribution));
    const results = await context.env.DB.batch([
      leadStatement,
      eventStatement(context.env.DB, lead, receivedAt, lead.lead_id),
    ]);
    const duplicate = results[0].meta?.changes === 0;
    if (duplicate) {
      const existing = await context.env.DB.prepare(`SELECT
        lead_event_id, email, design_id, submitted_at, experiment_id, brand_id, session_id,
        anonymous_visitor_id, cta_id, form_id, attribution_json
        FROM leads WHERE lead_id = ?`)
        .bind(lead.lead_id)
        .first();
      const expected = {
        lead_event_id: lead.event_id,
        email: lead.email,
        design_id: lead.design_id,
        submitted_at: lead.event_timestamp,
        experiment_id: lead.experiment_id,
        brand_id: lead.brand_id,
        session_id: lead.session_id,
        anonymous_visitor_id: lead.anonymous_visitor_id,
        cta_id: lead.cta_id,
        form_id: lead.form_id,
        attribution_json: JSON.stringify(attribution),
      };
      if (!existing || Object.keys(expected).some((field) => existing[field] !== expected[field])) {
        return json(409, { ok: false, error: 'submission_conflict' });
      }
    }
    return json(201, { ok: true, duplicate });
  } catch (error) {
    return handleError(error);
  }
}

export function onRequest() {
  return json(405, { ok: false, error: 'method_not_allowed' });
}
