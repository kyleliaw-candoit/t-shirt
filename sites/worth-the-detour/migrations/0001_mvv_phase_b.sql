CREATE TABLE IF NOT EXISTS leads (
  lead_id TEXT PRIMARY KEY,
  lead_event_id TEXT NOT NULL UNIQUE,
  email TEXT NOT NULL,
  design_id TEXT NOT NULL,
  submitted_at TEXT NOT NULL,
  server_received_at TEXT NOT NULL,
  experiment_id TEXT NOT NULL,
  brand_id TEXT NOT NULL,
  session_id TEXT NOT NULL,
  anonymous_visitor_id TEXT NOT NULL,
  cta_id TEXT NOT NULL,
  form_id TEXT NOT NULL,
  attribution_json TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS events (
  event_id TEXT PRIMARY KEY,
  event_name TEXT NOT NULL,
  event_timestamp TEXT NOT NULL,
  server_received_at TEXT NOT NULL,
  event_schema_version TEXT NOT NULL,
  experiment_id TEXT NOT NULL,
  brand_id TEXT NOT NULL,
  session_id TEXT NOT NULL,
  anonymous_visitor_id TEXT NOT NULL,
  page_url TEXT NOT NULL,
  page_path TEXT NOT NULL,
  referrer TEXT,
  device_type TEXT NOT NULL,
  viewport_width INTEGER NOT NULL,
  viewport_height INTEGER NOT NULL,
  attribution_json TEXT NOT NULL,
  properties_json TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS events_session_id_idx ON events(session_id);
CREATE INDEX IF NOT EXISTS events_name_design_idx ON events(event_name, json_extract(properties_json, '$.design_id'));
