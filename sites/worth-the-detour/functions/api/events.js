import { eventStatement, handleError, json, readJson, validateEvent } from '../_shared/server.js';

export async function onRequestPost(context) {
  try {
    if (!context.env.DB) return json(503, { ok: false, error: 'service_unavailable' });
    const event = validateEvent(await readJson(context.request));
    const result = await eventStatement(context.env.DB, event, new Date().toISOString()).run();
    return json(202, { ok: true, duplicate: result.meta?.changes === 0 });
  } catch (error) {
    return handleError(error);
  }
}

export function onRequest() {
  return json(405, { ok: false, error: 'method_not_allowed' });
}
