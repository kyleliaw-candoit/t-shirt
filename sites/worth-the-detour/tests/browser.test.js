import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import vm from 'node:vm';

const script = await readFile(new URL('../script.js', import.meta.url), 'utf8');
const DESIGN_IDS = ['B2', 'A1', 'A3', 'YIF-M', 'YIF-F', 'C2', 'C3B', 'Fashion-1D-F', 'Type-Led-3', 'Type-Led-4'];

class Storage {
  constructor() { this.values = new Map(); }
  getItem(key) { return this.values.get(key) ?? null; }
  setItem(key, value) { this.values.set(key, String(value)); }
}

class Element {
  constructor() {
    this.dataset = {};
    this.hidden = false;
    this.disabled = false;
    this.listeners = new Map();
    this.attributes = new Map();
    this.textContent = '';
  }
  addEventListener(name, handler) { this.listeners.set(name, handler); }
  dispatch(name, event = {}) { return this.listeners.get(name)?.({ target: this, currentTarget: this, preventDefault() {}, ...event }); }
  setAttribute(name, value) { this.attributes.set(name, String(value)); }
  removeAttribute(name) { this.attributes.delete(name); }
  focus() { this.focused = true; }
  showModal() { this.open = true; }
  close() { this.open = false; }
}

function harness({ width = 1440, leadResponse, sessionStorage = new Storage(), localStorage = new Storage(), search, now = 1_000 } = {}) {
  const globalListeners = new Map();
  const timers = new Map();
  const requests = [];
  let timerId = 0;
  let uuid = 0;
  const imageDialog = new Element();
  const enlargedImage = new Element();
  imageDialog.querySelector = (selector) => selector === 'img' ? enlargedImage : imageClose;
  const imageClose = new Element();
  const interestDialog = new Element();
  const interestProduct = new Element();
  const form = new Element();
  const email = new Element();
  email.validity = { valid: true };
  email.value = '';
  const submit = new Element();
  form.elements = { email };
  form.querySelector = () => submit;
  form.reset = () => { email.value = ''; };
  const emailError = new Element();
  emailError.textContent = 'Please enter a valid email address.';
  const success = new Element();
  success.hidden = true;
  const interestClose = new Element();
  interestDialog.querySelector = (selector) => {
    if (selector === '.interest-dialog__product') return interestProduct;
    if (selector === 'form') return form;
    if (selector === '.form-success') return success;
    return interestClose;
  };
  const products = DESIGN_IDS.map((designId) => {
    const product = new Element();
    product.dataset = { designId, productName: designId };
    const imageButton = new Element();
    const image = { currentSrc: `${designId}.png`, src: `${designId}.png`, alt: designId };
    imageButton.querySelector = () => image;
    imageButton.closest = () => product;
    const interestButton = new Element();
    interestButton.closest = () => product;
    return { product, imageButton, interestButton };
  });
  const selectors = {
    '.image-dialog': imageDialog,
    '#image-dialog-title': new Element(),
    '.interest-dialog': interestDialog,
    '#email-error': emailError,
  };
  const document = {
    referrer: 'https://example.org/source?private=discarded',
    documentElement: { scrollHeight: 5000 },
    querySelector: (selector) => selectors[selector],
    querySelectorAll: (selector) => {
      if (selector === '.product') return products.map(({ product }) => product);
      if (selector === '.product__image-button') return products.map(({ imageButton }) => imageButton);
      if (selector === '.interest-button') return products.map(({ interestButton }) => interestButton);
      return [];
    },
  };
  class FakeIntersectionObserver {
    constructor(callback) { this.callback = callback; observer.instance = this; }
    observe() {}
  }
  const observer = {};
  const defaultResponse = { ok: true };
  class FakeDate extends Date {
    constructor(...args) { super(...(args.length ? args : [now])); }
    static now() { return now; }
  }
  const context = {
    Blob, URL, URLSearchParams, console, document, Date: FakeDate,
    location: {
      search: search ?? '?creative_id=CR_TEST_A&utm_source=meta&meta_ad_id=META_AD_1',
      origin: 'https://worth-the-detour.com', pathname: '/',
    },
    innerWidth: width, innerHeight: 900, scrollY: 0,
    sessionStorage, localStorage,
    crypto: { randomUUID: () => `00000000-0000-4000-8000-${String(++uuid).padStart(12, '0')}` },
    fetch: async (url, options) => {
      const request = { url, body: JSON.parse(options.body) };
      requests.push(request);
      if (url === '/api/leads' && leadResponse) return leadResponse(request);
      return defaultResponse;
    },
    navigator: { sendBeacon: (url, body) => { requests.push({ url, beacon: body }); return true; } },
    IntersectionObserver: FakeIntersectionObserver,
    setTimeout: (callback) => { const id = ++timerId; timers.set(id, callback); return id; },
    clearTimeout: (id) => timers.delete(id),
    addEventListener: (name, callback) => globalListeners.set(name, callback),
  };
  vm.runInNewContext(script, context);
  return {
    context, document, products, form, email, emailError, success, imageDialog, interestDialog,
    requests, observer, timers, globalListeners,
    setNow(value) { now = value; },
    runTimers() { for (const [id, callback] of [...timers]) { timers.delete(id); callback(); } },
  };
}

const settle = () => new Promise((resolve) => setImmediate(resolve));

test('preserves acquisition creative while submitting a different selected design', async () => {
  let acceptLead;
  const pendingLead = new Promise((resolve) => { acceptLead = resolve; });
  const page = harness({ leadResponse: () => pendingLead });
  await settle();
  const selected = page.products.at(-1);
  selected.interestButton.dispatch('click');
  assert.equal(page.interestDialog.open, true);
  page.email.value = 'person@example.com';
  const submission = page.form.dispatch('submit');
  await settle();
  assert.equal(page.success.hidden, true, 'success remains hidden before server acceptance');
  const leadRequest = page.requests.find(({ url }) => url === '/api/leads');
  assert.equal(leadRequest.body.creative_id, 'CR_TEST_A');
  assert.equal(leadRequest.body.meta_ad_id, 'META_AD_1');
  assert.equal(leadRequest.body.design_id, 'Type-Led-4');
  acceptLead({ ok: true });
  await submission;
  assert.equal(page.success.hidden, false);
  const eventRequests = page.requests.filter(({ url }) => url === '/api/events').map(({ body }) => body);
  assert.equal(eventRequests.find(({ event_name }) => event_name === 'intent_click').design_id, 'Type-Led-4');
  assert.ok(eventRequests.every((event) => !('email' in event) && !JSON.stringify(event).includes('person@example.com')));
});

test('keeps first-touch attribution for later page loads in the same session', async () => {
  const sessionStorage = new Storage();
  const localStorage = new Storage();
  harness({ sessionStorage, localStorage });
  await settle();
  const laterPage = harness({ sessionStorage, localStorage, search: '' });
  await settle();
  const landing = laterPage.requests.find(({ body }) => body?.event_name === 'landing_view').body;
  assert.equal(landing.creative_id, 'CR_TEST_A');
  assert.equal(landing.utm_source, 'meta');
  assert.equal(landing.meta_ad_id, 'META_AD_1');
});

test('keeps the form open and reports a server/network failure', async () => {
  const page = harness({ leadResponse: async () => { throw new Error('offline'); } });
  await settle();
  page.products[0].interestButton.dispatch('click');
  page.email.value = 'person@example.com';
  await page.form.dispatch('submit');
  assert.equal(page.form.hidden, false);
  assert.equal(page.success.hidden, true);
  assert.equal(page.emailError.hidden, false);
  assert.equal(page.emailError.textContent, 'We could not save your email. Please try again.');
});

test('reuses a pending lead identity after an ambiguous failure', async () => {
  let attempts = 0;
  const page = harness({
    now: Date.parse('2026-08-22T12:00:00.000Z'),
    leadResponse: async () => {
      attempts += 1;
      if (attempts === 1) throw new Error('response_lost');
      return { ok: true };
    },
  });
  await settle();
  page.products[0].interestButton.dispatch('click');
  page.email.value = '  Person@Example.COM ';
  await page.form.dispatch('submit');
  page.email.value = 'person@example.com';
  await page.form.dispatch('submit');
  const [first, retry] = page.requests.filter(({ url }) => url === '/api/leads').map(({ body }) => body);
  assert.equal(retry.lead_id, first.lead_id);
  assert.equal(retry.event_id, first.event_id);
  assert.equal(retry.event_timestamp, first.event_timestamp);
  assert.equal(page.success.hidden, false);
});

test('replaces pending identity for changed input without leaking email to analytics', async () => {
  const page = harness({ leadResponse: async () => { throw new Error('offline'); } });
  await settle();
  page.products[0].interestButton.dispatch('click');
  page.email.value = 'first@example.com';
  await page.form.dispatch('submit');
  page.email.value = 'second@example.com';
  await page.form.dispatch('submit');
  page.products[1].interestButton.dispatch('click');
  page.email.value = 'second@example.com';
  await page.form.dispatch('submit');
  const leads = page.requests.filter(({ url }) => url === '/api/leads').map(({ body }) => body);
  assert.notEqual(leads[1].lead_id, leads[0].lead_id);
  assert.notEqual(leads[1].event_id, leads[0].event_id);
  assert.notEqual(leads[2].lead_id, leads[1].lead_id);
  assert.notEqual(leads[2].event_id, leads[1].event_id);
  const analytics = page.requests.filter(({ url }) => url === '/api/events');
  assert.ok(analytics.every(({ body }) => !JSON.stringify(body).includes('first@example.com')));
  assert.ok(analytics.every(({ body }) => !JSON.stringify(body).includes('second@example.com')));
  assert.ok(!JSON.stringify([...page.context.sessionStorage.values.values()]).includes('@example.com'));
  assert.ok(!JSON.stringify([...page.context.localStorage.values.values()]).includes('@example.com'));
});

test('keeps page_exit summaries cumulative across page loads in one session', async () => {
  const sessionStorage = new Storage();
  const localStorage = new Storage();
  const first = harness({ sessionStorage, localStorage, now: 1_000 });
  await settle();
  first.setNow(1_200);
  first.products[0].interestButton.dispatch('click');
  first.context.scrollY = 3_000;
  first.globalListeners.get('scroll')();
  first.observer.instance.callback([{ target: first.products[0].product, intersectionRatio: 0.5 }]);
  first.runTimers();
  first.setNow(2_000);
  first.globalListeners.get('pagehide')();
  const firstExit = JSON.parse(await first.requests.find(({ beacon }) => beacon).beacon.text());

  const second = harness({ sessionStorage, localStorage, now: 3_000 });
  await settle();
  second.products[0].interestButton.dispatch('click');
  second.observer.instance.callback([{ target: second.products[1].product, intersectionRatio: 0.5 }]);
  second.runTimers();
  second.setNow(4_000);
  second.globalListeners.get('pagehide')();
  const secondExit = JSON.parse(await second.requests.find(({ beacon }) => beacon).beacon.text());

  assert.equal(secondExit.session_id, firstExit.session_id);
  assert.equal(sessionStorage.getItem('wtd_mvv_session_started_at'), '1000');
  assert.ok(secondExit.session_duration_ms > firstExit.session_duration_ms);
  assert.ok(secondExit.max_scroll_depth >= firstExit.max_scroll_depth);
  assert.equal(secondExit.first_meaningful_engagement_ms, firstExit.first_meaningful_engagement_ms);
  assert.equal(firstExit.designs_viewed_count, 1);
  assert.equal(secondExit.designs_viewed_count, 2);
});

test('emits one design_view only after the one-second visibility timer', async () => {
  const page = harness();
  await settle();
  const product = page.products[0].product;
  page.observer.instance.callback([{ target: product, intersectionRatio: 0.5 }]);
  assert.equal(page.requests.filter(({ body }) => body?.event_name === 'design_view').length, 0);
  page.runTimers();
  await settle();
  const views = page.requests.filter(({ body }) => body?.event_name === 'design_view');
  assert.equal(views.length, 1);
  assert.equal(views[0].body.design_id, 'B2');
  assert.equal(views[0].body.view_duration_ms, 1000);
  page.observer.instance.callback([{ target: product, intersectionRatio: 0.5 }]);
  page.runTimers();
  await settle();
  assert.equal(page.requests.filter(({ body }) => body?.event_name === 'design_view').length, 1);
});

test('retains image/dialog behavior and mobile product-specific engagement', async () => {
  const page = harness({ width: 390 });
  await settle();
  page.products[2].imageButton.dispatch('click');
  await settle();
  assert.equal(page.imageDialog.open, true);
  const engagement = page.requests.find(({ body }) => body?.event_name === 'design_engagement').body;
  assert.equal(engagement.design_id, 'A3');
  assert.equal(engagement.interaction_type, 'image_expand');
  assert.equal(engagement.device_type, 'mobile');
});
