const EVENT_SCHEMA_VERSION = '0.1';
const EXPERIMENT_ID = 'mvv-r012-001';
const BRAND_ID = 'worth-the-detour';
const ATTRIBUTION_FIELDS = [
  'creative_territory_id', 'creative_id', 'variant_id', 'utm_source', 'utm_medium',
  'utm_campaign', 'utm_content', 'utm_term', 'fbclid', 'meta_campaign_id',
  'meta_adset_id', 'meta_ad_id',
];
const SESSION_KEY = 'wtd_mvv_session';
const VISITOR_KEY = 'wtd_mvv_visitor';
const VIEWS_KEY = 'wtd_mvv_design_views';
const SESSION_STARTED_KEY = 'wtd_mvv_session_started_at';
const MAX_SCROLL_KEY = 'wtd_mvv_max_scroll_depth';
const FIRST_ENGAGEMENT_KEY = 'wtd_mvv_first_engagement_ms';

function identifier(prefix) {
  return `${prefix}_${crypto.randomUUID()}`;
}

function storedIdentifier(storage, key, prefix) {
  let value = storage.getItem(key);
  if (!value) {
    value = identifier(prefix);
    storage.setItem(key, value);
  }
  return value;
}

const sessionId = storedIdentifier(sessionStorage, SESSION_KEY, 'ses');
let sessionStartedAt = Number(sessionStorage.getItem(SESSION_STARTED_KEY));
if (!Number.isFinite(sessionStartedAt) || sessionStartedAt <= 0) {
  sessionStartedAt = Date.now();
  sessionStorage.setItem(SESSION_STARTED_KEY, String(sessionStartedAt));
}
let anonymousVisitorId;
try {
  anonymousVisitorId = storedIdentifier(localStorage, VISITOR_KEY, 'av');
} catch {
  anonymousVisitorId = storedIdentifier(sessionStorage, VISITOR_KEY, 'av');
}

const query = new URLSearchParams(location.search);
const storedAttribution = JSON.parse(sessionStorage.getItem('wtd_mvv_attribution') || '{}');
for (const field of ATTRIBUTION_FIELDS) {
  if (!(field in storedAttribution) && query.has(field) && query.get(field)) {
    storedAttribution[field] = query.get(field).slice(0, field === 'fbclid' ? 512 : 256);
  }
}
sessionStorage.setItem('wtd_mvv_attribution', JSON.stringify(storedAttribution));

const viewedDesigns = new Set(JSON.parse(sessionStorage.getItem(VIEWS_KEY) || '[]'));
const storedFirstEngagement = sessionStorage.getItem(FIRST_ENGAGEMENT_KEY);
let firstMeaningfulEngagementMs = storedFirstEngagement === null ? null : Number(storedFirstEngagement);
let maxScrollDepth = Number(sessionStorage.getItem(MAX_SCROLL_KEY)) || 0;
let exitSent = false;
let pendingLeadSubmission = null;

function deviceType() {
  if (innerWidth < 768) return 'mobile';
  if (innerWidth < 1024) return 'tablet';
  return 'desktop';
}

function envelope(eventName, properties = {}) {
  const cleanUrl = `${location.origin}${location.pathname}`;
  return {
    event_name: eventName,
    event_id: identifier('evt'),
    event_timestamp: new Date().toISOString(),
    event_schema_version: EVENT_SCHEMA_VERSION,
    experiment_id: EXPERIMENT_ID,
    brand_id: BRAND_ID,
    session_id: sessionId,
    anonymous_visitor_id: anonymousVisitorId,
    page_url: cleanUrl,
    page_path: location.pathname,
    referrer: document.referrer ? document.referrer.split('?')[0] : null,
    device_type: deviceType(),
    viewport_width: innerWidth,
    viewport_height: innerHeight,
    ...storedAttribution,
    ...properties,
  };
}

async function sendEvent(eventName, properties = {}) {
  const response = await fetch('/api/events', {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify(envelope(eventName, properties)),
    keepalive: true,
  });
  if (!response.ok) throw new Error('event_delivery_failed');
}

function markMeaningfulEngagement() {
  if (firstMeaningfulEngagementMs === null) {
    firstMeaningfulEngagementMs = Math.max(0, Date.now() - sessionStartedAt);
    sessionStorage.setItem(FIRST_ENGAGEMENT_KEY, String(firstMeaningfulEngagementMs));
  }
}

const imageDialog = document.querySelector('.image-dialog');
const enlargedImage = imageDialog.querySelector('img');
const imageDialogTitle = document.querySelector('#image-dialog-title');
const interestDialog = document.querySelector('.interest-dialog');
const interestProduct = interestDialog.querySelector('.interest-dialog__product');
const interestForm = interestDialog.querySelector('form');
const emailInput = interestForm.elements.email;
const emailError = document.querySelector('#email-error');
const successMessage = interestDialog.querySelector('.form-success');
const submitButton = interestForm.querySelector('button[type="submit"]');
const validationMessage = emailError.textContent;

function closeOnBackdrop(event) {
  if (event.target === event.currentTarget) event.currentTarget.close();
}

document.querySelectorAll('.product__image-button').forEach((button) => {
  button.addEventListener('click', () => {
    const product = button.closest('.product');
    const sourceImage = button.querySelector('img');
    enlargedImage.src = sourceImage.currentSrc || sourceImage.src;
    enlargedImage.alt = sourceImage.alt;
    imageDialogTitle.textContent = product.dataset.productName;
    imageDialog.showModal();
    markMeaningfulEngagement();
    sendEvent('design_engagement', { design_id: product.dataset.designId, interaction_type: 'image_expand' }).catch(() => {});
  });
});

document.querySelectorAll('.interest-button').forEach((button) => {
  button.addEventListener('click', () => {
    const product = button.closest('.product');
    interestProduct.textContent = product.dataset.productName;
    interestForm.dataset.designId = product.dataset.designId;
    interestForm.reset();
    interestForm.hidden = false;
    interestForm.removeAttribute('aria-busy');
    submitButton.disabled = false;
    emailError.textContent = validationMessage;
    emailError.hidden = true;
    successMessage.hidden = true;
    emailInput.removeAttribute('aria-invalid');
    interestDialog.showModal();
    markMeaningfulEngagement();
    sendEvent('intent_click', {
      design_id: product.dataset.designId,
      cta_id: 'design-interest',
      cta_location: 'design_card',
    }).catch(() => {});
  });
});

imageDialog.querySelector('.image-dialog__close').addEventListener('click', () => imageDialog.close());
interestDialog.querySelector('.interest-dialog__close').addEventListener('click', () => interestDialog.close());
imageDialog.addEventListener('click', closeOnBackdrop);
interestDialog.addEventListener('click', closeOnBackdrop);

interestForm.addEventListener('submit', async (event) => {
  event.preventDefault();
  if (!emailInput.validity.valid) {
    emailError.textContent = validationMessage;
    emailError.hidden = false;
    emailInput.setAttribute('aria-invalid', 'true');
    emailInput.focus();
    return;
  }

  emailError.hidden = true;
  emailInput.removeAttribute('aria-invalid');
  interestForm.setAttribute('aria-busy', 'true');
  submitButton.disabled = true;
  const normalizedEmail = emailInput.value.trim().toLowerCase();
  const designId = interestForm.dataset.designId;
  if (!pendingLeadSubmission
      || pendingLeadSubmission.normalizedEmail !== normalizedEmail
      || pendingLeadSubmission.designId !== designId) {
    const leadEvent = envelope('lead_submit', {
      design_id: designId,
      cta_id: 'design-interest',
      form_id: 'availability-interest',
    });
    pendingLeadSubmission = {
      normalizedEmail,
      designId,
      leadId: identifier('lead'),
      eventId: leadEvent.event_id,
      eventTimestamp: leadEvent.event_timestamp,
      leadEvent,
    };
  }
  const lead = {
    ...pendingLeadSubmission.leadEvent,
    event_id: pendingLeadSubmission.eventId,
    event_timestamp: pendingLeadSubmission.eventTimestamp,
    lead_id: pendingLeadSubmission.leadId,
    email: normalizedEmail,
  };
  delete lead.event_name;

  try {
    const response = await fetch('/api/leads', {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify(lead),
    });
    if (!response.ok) throw new Error('lead_delivery_failed');
    pendingLeadSubmission = null;
    interestForm.hidden = true;
    successMessage.hidden = false;
    successMessage.focus();
  } catch {
    emailError.textContent = 'We could not save your email. Please try again.';
    emailError.hidden = false;
    submitButton.disabled = false;
  } finally {
    interestForm.removeAttribute('aria-busy');
  }
});

const visibilityTimers = new Map();
const observer = new IntersectionObserver((entries) => {
  for (const entry of entries) {
    const product = entry.target;
    const designId = product.dataset.designId;
    if (entry.intersectionRatio >= 0.5 && !viewedDesigns.has(designId) && !visibilityTimers.has(designId)) {
      const startedAt = Date.now();
      const timer = setTimeout(() => {
        visibilityTimers.delete(designId);
        if (!viewedDesigns.has(designId)) {
          viewedDesigns.add(designId);
          sessionStorage.setItem(VIEWS_KEY, JSON.stringify([...viewedDesigns]));
          sendEvent('design_view', {
            design_id: designId,
            design_position: Number(product.dataset.designPosition),
            view_duration_ms: Math.max(1000, Date.now() - startedAt),
          }).catch(() => {});
        }
      }, 1000);
      visibilityTimers.set(designId, timer);
    } else if (entry.intersectionRatio < 0.5 && visibilityTimers.has(designId)) {
      clearTimeout(visibilityTimers.get(designId));
      visibilityTimers.delete(designId);
    }
  }
}, { threshold: [0, 0.5, 1] });

document.querySelectorAll('.product').forEach((product, index) => {
  product.dataset.designPosition = String(index + 1);
  observer.observe(product);
});

function updateScrollDepth() {
  const available = document.documentElement.scrollHeight - innerHeight;
  const depth = available <= 0 ? 100 : Math.round(((scrollY + innerHeight) / document.documentElement.scrollHeight) * 100);
  const observedDepth = Math.min(100, depth);
  if (observedDepth > maxScrollDepth) {
    maxScrollDepth = observedDepth;
    sessionStorage.setItem(MAX_SCROLL_KEY, String(maxScrollDepth));
  }
}
addEventListener('scroll', updateScrollDepth, { passive: true });
updateScrollDepth();

function sendExit() {
  if (exitSent) return;
  exitSent = true;
  const payload = envelope('page_exit', {
    session_duration_ms: Math.max(0, Date.now() - sessionStartedAt),
    max_scroll_depth: maxScrollDepth,
    designs_viewed_count: viewedDesigns.size,
    first_meaningful_engagement_ms: firstMeaningfulEngagementMs,
  });
  navigator.sendBeacon('/api/events', new Blob([JSON.stringify(payload)], { type: 'application/json' }));
}
addEventListener('pagehide', sendExit);

sendEvent('landing_view').catch(() => {});
