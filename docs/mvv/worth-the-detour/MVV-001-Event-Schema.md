---
title: MVV-001 Event Schema
brand: Worth the Detour
experiment_id: mvv-r012-001
status: Proposed
version: 0.1
last_updated: 2026-08-17
governing_methodology: docs/company/Minimum-Viable-Validation-Methodology.md
---

# MVV-001 Event Schema

## 1. Purpose

This document is the canonical instrumentation contract for **Worth the Detour MVV #1**.

It translates the company’s Minimum Viable Validation Methodology into the minimum event and attribution schema needed to connect paid Meta traffic to landing-page behavior and downstream intent.

The implementation objective is:

> **Meta impression / click → persistent creative and design identity → landing visit → meaningful engagement → intent**

This schema is deliberately narrow. It exists to support MVV #1 learning, not to create a general analytics platform.

Page implementations must conform to this schema. Do not add, rename, or reinterpret events or persistent experiment identifiers without updating this document first.

No Shopify, POD, checkout, purchase infrastructure, data warehouse, session replay, heatmaps, or other unearned infrastructure is required for MVV #1.

---

## 2. Governing MVV Principle

The Minimum Viable Validation Methodology governs this implementation.

MVV #1 should preserve the ability to diagnose evidence at the narrowest justified hypothesis level. In particular, the analytics layer must allow performance to be attributed to the specific creative territory, creative, design, and variant that generated the traffic.

The measurement system should therefore answer:

1. Which ad / creative brought the visitor?
2. Which design or execution was being tested?
3. Did the visitor actually consume the landing page?
4. Which design(s) did the visitor meaningfully see?
5. Did the visitor show meaningful engagement?
6. Did the visitor express stronger intent?
7. Did the visitor submit contact information?

The system should not collect data merely because it is technically possible to collect it.

---

## 3. Schema Version

Every event must carry:

```text
event_schema_version = 0.1
```

If event definitions or required properties materially change, increment the schema version and update this document before deployment.

---

## 4. Persistent Experiment Identity

The following identifiers form the experiment identity chain. They must remain stable from the incoming ad URL through the landing-page session and all downstream events where applicable.

| Property | Purpose | Requirement |
|---|---|---|
| `experiment_id` | Identifies the MVV experiment | Required |
| `brand_id` | Identifies the brand | Required |
| `creative_territory_id` | Identifies the creative territory hypothesis | Required when applicable |
| `creative_id` | Identifies the ad / creative execution | Required for paid Meta traffic |
| `design_id` | Identifies the product/design execution | Required when a specific design is represented |
| `variant_id` | Identifies a presentation or execution variant | Required when variants exist |

For MVV #1:

```text
experiment_id = mvv-r012-001
brand_id = worth-the-detour
```

`creative_territory_id`, `creative_id`, `design_id`, and `variant_id` must use the same stable identifiers as the canonical Creative Director / MVV source records. The landing-page implementation must not invent a second identifier system.

### 4.1 R012 `design_id` convention

For MVV #1, the existing canonical Creative Director identifiers **are the `design_id` values**. Do not create a parallel remapping such as `D001`, `D002`, or `D007` for designs that already have established identifiers.

Examples of valid canonical `design_id` values include:

```text
B1
B2
A1
C2
C3B
YIF-M
Fashion-1C
Fashion-1D
Fashion-7A1
Fashion-7A2
Type-Led-3
Type-Led-4
```

This list is illustrative of the current locked R012 records, not a requirement that every listed design appear in the final MVV #1 landing-page assortment.

Where a founder-approved locked execution already has its own canonical identifier, such as `YIF-M`, use that exact identifier as `design_id`. Do not decompose it into a newly invented parent `design_id` plus `variant_id` unless the canonical Creative Director record is explicitly revised to define that structure.

`variant_id` remains available for a distinct presentation or execution variant when such a variant is separately defined by the canonical source records; it must not be used merely to reconstruct an existing canonical design identifier.

If an identifier is not applicable to a particular event, it may be null or omitted according to the implementation convention, but its meaning must not be repurposed.

---

## 5. Traffic Attribution Properties

Capture incoming campaign attribution on the first landing-page request where available, then preserve it for the duration of the session.

| Property | Purpose |
|---|---|
| `utm_source` | Traffic source, e.g. `meta` |
| `utm_medium` | Traffic medium, e.g. `paid-social` |
| `utm_campaign` | Campaign naming / experiment mapping |
| `utm_content` | Creative or content-level attribution |
| `utm_term` | Optional audience / targeting label |
| `fbclid` | Meta click identifier when present |
| `meta_campaign_id` | Meta campaign ID when explicitly passed |
| `meta_adset_id` | Meta ad set ID when explicitly passed |
| `meta_ad_id` | Meta ad ID when explicitly passed |

### 5.1 Attribution Rule

Meta platform identifiers explain **where traffic came from**.

Company-controlled persistent identifiers explain **which hypothesis was being tested**.

Do not rely on Meta campaign or ad naming alone to identify a creative or design.

### 5.2 Example Landing URL

```text
https://worth-the-detour.com/
?experiment_id=mvv-r012-001
&creative_id=CR003
&design_id=B1
&utm_source=meta
&utm_medium=paid-social
&utm_campaign=mvv-r012-001
&utm_content=CR003
```

The exact creative/design IDs in production must match the canonical records.

---

## 6. Common Event Envelope

All first-party landing-page events must include the following common fields when available.

### Required

```text
event_name
event_id
event_timestamp
event_schema_version
experiment_id
brand_id
session_id
anonymous_visitor_id
page_url
page_path
```

### Persistent hypothesis / attribution context

```text
creative_territory_id
creative_id
design_id
variant_id
utm_source
utm_medium
utm_campaign
utm_content
utm_term
fbclid
meta_campaign_id
meta_adset_id
meta_ad_id
```

### Diagnostic page context

```text
referrer
device_type
viewport_width
viewport_height
```

`event_id` must be unique per emitted event so duplicate events can be detected or de-duplicated downstream.

`session_id` should represent one browsing session.

`anonymous_visitor_id` may persist across sessions only if the implementation can do so simply and lawfully without fingerprinting. MVV #1 does not require sophisticated identity resolution.

---

# 7. Canonical Events

MVV #1 uses six first-party landing-page events.

## 7.1 `landing_view`

### Purpose

Record a successfully loaded landing-page visit.

### Fire when

The landing page has loaded sufficiently for the visitor to view the primary experience and the analytics layer is initialized.

### Event-specific properties

```text
landing_variant_id
```

### Notes

- Fire once per page load / route view.
- This is the denominator for raw landing-page conversion.
- A `landing_view` alone must not be treated as evidence that the visitor intentionally consumed the page.

---

## 7.2 `design_view`

### Purpose

Record that a specific design became meaningfully visible to the visitor.

### Fire when

A design satisfies the implementation’s meaningful-visibility rule.

Recommended initial rule:

- at least 50% of the design presentation is visible in the viewport, and
- it remains visible for at least 1 second.

The coding layer may adjust the implementation mechanics if required by browser behavior, but must preserve the concept of **meaningful exposure**, not mere DOM presence.

### Event-specific properties

```text
design_id
design_position
view_duration_ms
```

### Notes

- Fire once per design per page session unless there is a clear analytical reason to count repeated exposures separately.
- `design_position` identifies where the design appeared in the page experience.

---

## 7.3 `design_engagement`

### Purpose

Record deliberate interaction with a specific design.

### Fire when

The visitor intentionally interacts with a design presentation.

### Event-specific properties

```text
design_id
interaction_type
```

Initial supported `interaction_type` values:

```text
tap
image_expand
hover
```

### Notes

- `hover` is diagnostic only and should not be treated as a primary MVV success signal.
- Prefer explicit interactions such as taps or image expansion over passive mouse movement.
- Do not implement continuous mouse-coordinate tracking.

---

## 7.4 `intent_click`

### Purpose

Record a visitor taking the principal pre-lead intent action.

Examples include clicking a CTA such as “I want this,” “Notify me,” or an equivalent MVV-specific intent action.

### Fire when

The visitor activates the relevant CTA.

### Event-specific properties

```text
design_id
cta_id
cta_location
```

### Notes

- `cta_id` must be stable and implementation-defined.
- `cta_location` should identify where the CTA appeared, e.g. hero, design card, sticky CTA, or footer.
- If the CTA is associated with a specific design, `design_id` is required.

---

## 7.5 `lead_submit`

### Purpose

Record successful submission of email / waitlist contact information.

### Fire when

The form submission has been successfully accepted, not merely when the submit button is clicked.

### Event-specific properties

```text
design_id
cta_id
form_id
```

### Privacy rule

Do **not** put the submitted email address, name, or other personally identifying form values into the analytics event payload.

If lead information is collected, store it in the minimum appropriate lead-storage system separately from behavioral analytics.

---

## 7.6 `page_exit`

### Purpose

Capture best-effort session summary information for diagnostics.

### Fire when

The implementation can reasonably detect page/session termination or navigation away.

### Event-specific properties

```text
session_duration_ms
max_scroll_depth
designs_viewed_count
first_meaningful_engagement_ms
```

### Notes

- Browser exit events are inherently imperfect.
- `page_exit` must not be used as a primary validation metric.
- Session-summary values may alternatively be computed downstream if doing so is simpler and more reliable.

---

# 8. Session Quality and Accidental-Click Filtering

MVV #1 must distinguish raw paid arrivals from sessions that show evidence of intentional page consumption.

The system must **not** emit an `accidental_click` event because visitor intent cannot be known with certainty.

Instead, derive session quality from observable behavior.

## 8.1 Required session-quality inputs

The implementation must make it possible to derive:

```text
session_duration_ms
max_scroll_depth
designs_viewed_count
first_meaningful_engagement_ms
```

The canonical events already provide or support these values.

## 8.2 Derived session classifications

Initial analytical classifications:

```text
bounce_like
engaged
high_intent
```

These are **derived metrics**, not browser events.

### `bounce_like`

A session that contains a `landing_view` but shows little or no evidence that the visitor intentionally consumed the page.

Typical pattern:

- very short session,
- no meaningful design view,
- no meaningful scroll,
- no design engagement,
- no intent click,
- no lead submit.

### `engaged`

A session showing evidence that the visitor intentionally consumed the page.

A session may qualify as engaged when it satisfies at least one meaningful criterion, such as:

- meaningful design view,
- meaningful scroll beyond the initial viewport,
- deliberate design engagement,
- sufficient time on page,
- intent click,
- lead submit.

Exact numerical thresholds should be treated as calibration hypotheses and may be adjusted after inspecting MVV #1 behavior.

### `high_intent`

A session containing either:

```text
intent_click
```

or:

```text
lead_submit
```

`lead_submit` represents the stronger signal.

## 8.3 Reporting Rule

Report both:

```text
lead_submit / landing_view
```

and, where useful:

```text
lead_submit / engaged_session
```

This preserves two distinct questions:

1. How effectively does paid traffic convert overall?
2. How effectively does the landing experience convert visitors who actually engage?

This distinction helps diagnose traffic-quality / accidental-click effects separately from landing-page or offer weakness.

---

# 9. Derived Funnel Metrics

The schema must support the following minimum funnel.

```text
Meta impression
→ Meta click
→ landing_view
→ engaged_session
→ design_view
→ intent_click
→ lead_submit
```

Meta impressions and ad clicks may originate from Meta reporting rather than first-party browser events.

## 9.1 Core MVV metrics

### Ad layer

- impressions
- clicks
- CTR
- CPC

### Landing layer

- raw landing visits
- click-to-landing arrival rate
- engaged-session rate
- design exposure rate
- design engagement rate
- intent-click rate
- lead conversion rate

### Cross-funnel

- impression → landing visit
- ad click → landing visit
- landing visit → engaged session
- landing visit → intent
- landing visit → lead
- engaged session → intent
- engaged session → lead
- creative / design → downstream intent

The coding layer should instrument raw events. Analytical ratios should be computed downstream rather than emitted as separate browser events.

---

# 10. Implementation Rules

## 10.1 Persist attribution within the session

On entry, parse the experiment and traffic-attribution values from the landing URL and preserve them for all subsequent events in the same session.

A downstream event must not lose its source creative / design identity simply because URL parameters are no longer visible after interaction or navigation.

## 10.2 Preserve company IDs independently of Meta IDs

Meta IDs and company-controlled IDs must remain separate fields.

Do not overwrite `creative_id` with `meta_ad_id`, or `design_id` with ad naming conventions.

## 10.3 One semantic meaning per property

Do not reuse a property for a different concept because a value is temporarily unavailable.

For example:

- `creative_id` always means the company creative ID.
- `design_id` always means the canonical design ID.
- `meta_ad_id` always means the Meta ad ID.

## 10.4 Missing values

Missing attribution values are acceptable when traffic did not provide them.

The implementation must not invent synthetic values that could later be mistaken for real campaign attribution.

## 10.5 Event de-duplication

Generate a unique `event_id` for every emitted event.

Where an event should fire only once, such as a design’s first meaningful view in a session, the page implementation should suppress unintended duplicate firing.

---

# 11. Privacy and Data Minimization

MVV #1 should collect only what is needed to make the experiment decision.

Do not collect or derive unnecessarily:

- names in analytics payloads,
- email addresses in analytics payloads,
- precise geolocation,
- browser fingerprinting attributes,
- continuous mouse coordinates,
- session replay,
- sensitive personal information,
- cross-device identity graphs.

If an anonymous visitor identifier is used, prefer a simple first-party pseudonymous value over fingerprinting.

---

# 12. Explicitly Out of Scope for MVV #1

Do not implement the following unless a later experiment explicitly earns the complexity:

- Shopify analytics,
- POD integration tracking,
- checkout events,
- purchase events,
- refunds / cancellations,
- Meta Conversions API,
- server-side attribution platform,
- data warehouse,
- customer data platform,
- heatmaps,
- session replay,
- continuous mouse tracking,
- generalized multi-brand analytics architecture,
- cross-device identity resolution,
- elaborate consent-management infrastructure beyond what the actual deployed tooling and applicable requirements necessitate.

---

# 13. Coding-Layer Acceptance Criteria

Before MVV #1 is considered instrumented, verify all of the following.

- [ ] `landing_view` fires correctly.
- [ ] `design_view` fires only after meaningful visibility.
- [ ] `design_engagement` fires only for defined interactions.
- [ ] `intent_click` fires with stable CTA identity.
- [ ] `lead_submit` fires only after successful lead capture.
- [ ] `page_exit` or equivalent session-summary logic supplies required diagnostic fields where technically reliable.
- [ ] `event_schema_version = 0.1` is present on every event.
- [ ] `experiment_id = mvv-r012-001` persists across the session.
- [ ] `brand_id = worth-the-detour` persists across the session.
- [ ] canonical creative / design IDs persist from incoming traffic to downstream events.
- [ ] existing canonical Creative Director identifiers are used directly as `design_id`; no parallel `D###` remapping is introduced.
- [ ] Meta IDs remain separate from company-controlled IDs.
- [ ] UTM values persist across the session where supplied.
- [ ] a unique `event_id` is generated for each event.
- [ ] duplicate one-time events are suppressed.
- [ ] analytics payloads contain no submitted email address or name.
- [ ] raw landing visits can be distinguished from derived engaged sessions.
- [ ] events can be inspected in the chosen analytics/debugging layer before paid traffic is launched.

---

# 14. Change Control

This document is the source of truth for MVV #1 instrumentation behavior.

If implementation reveals that an event, property, or threshold is inadequate:

1. identify the learning or implementation problem,
2. make the smallest schema change that solves it,
3. update this document,
4. increment the schema version when semantics materially change,
5. then update the page instrumentation.

Do not silently change event semantics in code.

---

# 15. Next Step

After this schema is approved, the next layer is to establish the minimum GitHub + Cloudflare Pages page-building and deployment path.

No landing-page code should be written before this event schema is accepted as the instrumentation contract for MVV #1.
