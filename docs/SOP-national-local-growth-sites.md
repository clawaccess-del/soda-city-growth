# SOP - Reusable Local Growth Website System

## Purpose

Use this SOP to clone the Soda City Growth model into new cities and metro areas without rebuilding the strategy from scratch.

This system is not just a brochure website. It is a local lead-generation site built around one integrated offer stack:

- free website build for qualifying businesses
- six-month growth partnership tied to the free build
- local SEO
- Google Business Profile management
- monthly Google Business Profile posts
- citation support
- Google Ads / paid traffic support
- AI-ready page structure and FAQs
- small-roster positioning for faster support

## Entity separation rule

This rule applies only to the local marketing websites built from this Soda City Growth market-site SOP.
It does not automatically apply to unrelated websites in other project lines.

Every website built from this SOP must be treated as a separate business entity.

That means:

- no cross-linking between sibling market websites unless explicitly approved later
- no public references from one market brand/site to another market brand/site
- no mixed project notes across websites
- no shared contact details, proofs, or brand claims unless they are intentionally and explicitly the same business
- reuse the framework internally, but keep the finished websites operationally and publicly separate

## What is already baked into the Soda City Growth model

### Offer architecture

The website is built around these positioning choices:

- The website is the foundation, not the whole service.
- The free website offer is a foot-in-the-door offer for qualifying businesses.
- The free build is tied to a six-month contract because of the upfront research, planning, keyword work, structure planning, topic planning, and industry research.
- Ongoing value comes from the full growth stack after launch.
- The roster is capped at 15 active clients to make the service feel more direct and responsive.
- Messaging stays outcome-focused: better visibility, better trust, better lead flow, better conversion paths.

### Site architecture

Every market-clone site should include at minimum:

- Homepage
- Contact page
- Free website offer page
- Web design page
- Local SEO + Google Business Profile + AI visibility page
- Google Ads page
- Primary city page
- 4 to 8 supporting area pages
- robots.txt
- sitemap.xml
- favicon
- shared CSS
- shared JS for mobile nav and contact form behavior

### SEO / schema architecture

The current framework includes:

- unique title tag and meta description for every page
- canonical URL on every page
- Open Graph metadata on key pages
- JSON-LD schema that matches what is actually on the page
- FAQ schema on pages with FAQ sections
- Service schema on service pages
- Organization, WebSite, and WebPage schema on the homepage
- ContactPage schema on the contact page
- BreadcrumbList schema on interior pages
- sitemap.xml containing all live URLs
- robots.txt pointing to sitemap.xml

### UX / conversion architecture

The current framework includes:

- sticky header
- prominent phone CTA in navigation
- phone CTA repeated in hero sections and footer
- mobile-friendly layout
- contact form that captures:
  - name
  - phone
  - email
  - business
  - service interest
  - notes
- current form action opens a prefilled text draft to the business number
- CTA language focused on calling, texting, or sending details fast

### Copy architecture

The current model uses these copy rules:

- lead with the client outcome, not agency chest-beating
- position the site as the base layer for SEO, GBP, citations, and ads
- explain the six-month contract clearly, but do not lead the homepage with contract mechanics
- keep the homepage benefit-led
- use deeper pages to explain qualification logic and contract structure
- make area pages distinct enough that they do not read like thin city swaps
- avoid fake authority signals, fake numbers, fake testimonials, fake addresses, or fake case studies
- keep schema conservative and supportable

## Required inputs before building a new market site

Do not start cloning until these inputs are gathered.

### Brand and routing inputs

- brand name
- production domain
- phone number
- phone number in display format and E.164 format
- public email address, if available
- preferred contact path:
  - call only
  - text
  - form to SMS
  - form to inbox
  - booking link

### Market inputs

- primary city
- state name
- state abbreviation
- metro label
- 4 to 8 secondary service areas
- target industries or business categories
- any neighborhoods or nearby towns worth referencing

### Offer inputs

- whether the free website offer stays unchanged
- whether the six-month term stays unchanged
- whether the 15-client cap stays unchanged
- exact service mix offered in that market
- qualification rules
- disqualifying business types, if any

### Proof and trust inputs

- testimonials
- case studies
- portfolio screenshots
- before/after examples
- certifications or partner badges
- owner bio or founder story, if you want a more personal version

## Standard build sequence

### Phase 1: market strategy

1. Confirm the brand, phone, domain, and routing.
2. Confirm the primary city and supporting cities.
3. Confirm whether the market is city-first, metro-first, or region-first.
4. Confirm the service categories to emphasize.
5. Confirm whether the free-build plus six-month model is unchanged.
6. Collect any proof assets that are safe to publish.

### Phase 2: local research

1. Identify the main local-intent search patterns for the primary city.
2. Identify 4 to 8 adjacent service areas that are commercially relevant.
3. Note local phrasing, landmarks, commuter patterns, or geo references that help copy feel real.
4. Check how competitors frame web design, SEO, GBP, and Google Ads.
5. Decide which areas deserve dedicated pages now versus later.

### Phase 3: site setup

1. Duplicate the base repo or starter files.
2. Replace brand name, domain, phone, and city tokens globally.
3. Update favicon or brand mark if needed.
4. Update canonical URLs and all schema URLs.
5. Update areaServed arrays.
6. Update robots.txt and sitemap.xml.

### Phase 4: homepage build

1. Rewrite hero for the new market.
2. Update area strip with the real metro ring.
3. Keep the value proposition outcome-led.
4. Keep the integrated service stack visible.
5. Keep the roster-cap positioning if still true.
6. Keep the FAQ grounded in real offers and real constraints.

### Phase 5: service page build

Build these pages:

- free website offer page
- web design page
- local SEO + GBP + AI visibility page
- Google Ads page

For each page:

1. Make the title city-specific.
2. Make the page angle specific to that service.
3. Keep cross-links to the other services.
4. Keep 3 to 6 FAQs that answer real objections.
5. Make the page clearly support the overall growth model.

### Phase 6: area page build

1. Create one page per selected secondary market.
2. Do not just swap city names.
3. Give each page a distinct angle based on market behavior, trust profile, or demand shape.
4. Link area pages back to service pages.
5. Keep schema scoped to the actual area page.

### Phase 7: contact page build

1. Update phone, email, and form routing.
2. Keep form fields aligned with lead qualification.
3. Make the direct-contact path obvious.
4. If email is not verified, do not publish one.

### Phase 8: QA and launch

1. Test every internal link.
2. Test every phone link.
3. Test SMS or form behavior on mobile.
4. Validate schema JSON syntax.
5. Confirm sitemap.xml contains all live pages.
6. Confirm robots.txt points to the right sitemap.
7. Check titles, descriptions, canonicals, and OG tags.
8. Review for leftover city, phone, brand, or domain references from the previous market.
9. Deploy to staging or production.
10. Smoke test the live site.

## Page-level framework

### Homepage

Must include:

- market-specific title and description
- hero that leads with outcome
- two strong CTAs
- explanation that the site is the foundation for the broader growth stack
- core benefits section
- service stack explanation
- small-roster or direct-support differentiator
- service links
- service-area links
- contact CTA block
- FAQ block
- Organization + WebSite + WebPage schema

### Free website offer page

Must include:

- what the offer is
- who qualifies
- why the free build exists
- why it is tied to a six-month contract
- how it supports later SEO / GBP / ads
- FAQ answering objections
- Service schema + FAQ schema + breadcrumb schema

### Web design page

Must include:

- why the website comes first
- what the build improves
- how it supports SEO and ads
- mobile and conversion framing
- FAQ

### SEO + GBP + AI visibility page

Must include:

- what local visibility includes
- Google Business Profile management
- monthly posts
- citation support
- honest schema and FAQ logic
- AI-ready explanation without hype
- FAQ

### Google Ads page

Must include:

- why page quality matters to paid traffic
- landing page alignment
- local messaging alignment
- relationship between paid and organic pages
- FAQ

### Area pages

Must include:

- city-specific title and meta description
- a distinct angle for that city
- why the market needs clarity / trust / conversion support
- how the full service stack applies locally
- links back to core service pages
- Service or WebPage schema scoped to that page

### Contact page

Must include:

- direct phone CTA
- optional text CTA
- lead form
- explanation of what to send
- clarity on available contact channels
- ContactPage schema + breadcrumb schema

## Copy rules that must stay consistent across markets

### Keep

- client-facing language
- local language that sounds grounded
- integrated service-stack framing
- clear CTAs
- honest FAQs
- realistic qualification language
- conservative schema

### Avoid

- generic agency fluff
- fake social proof
- unsupported review stars or ratings
- fake addresses
- fake team size claims
- overpromising rankings
- stuffing city names unnaturally
- duplicating area pages with near-identical copy

## Reusable messaging pillars

Every cloned site should keep these pillars unless the offer changes.

### Pillar 1: Fix the website first

The website is the base layer that makes SEO, GBP, citations, and Google Ads more effective.

### Pillar 2: Better visibility and better lead flow

The work is framed around clearer trust, clearer messaging, clearer next steps, and stronger local presence.

### Pillar 3: Integrated local growth stack

The site, Google Business Profile, monthly posts, citations, and ads should reinforce one another.

### Pillar 4: Smaller roster, more direct support

The capped-client model is used as a differentiation point if it remains true.

### Pillar 5: Honest local SEO

Schema, FAQs, and location references should clarify what is true, not invent it.

## Technical standards

- Keep the site lightweight and static by default.
- Keep CSS and JS shared when possible.
- Keep nav and CTA patterns consistent across pages.
- Keep forms simple.
- Use one primary phone number consistently across headers, hero blocks, footer, schema, and contact page.
- Use production-domain canonicals before launch.
- Replace any temporary Vercel URLs when the live domain is ready.

## Expansion rules for national rollout

When cloning this system into multiple markets:

- keep one shared starter framework
- replace market tokens systematically
- prioritize one primary city plus a tight metro ring first
- do not launch dozens of thin area pages at once
- create deeper proof assets over time so later markets launch stronger than earlier ones
- standardize what changes by market versus what stays global
- treat every launched website in this market-site portfolio as a separate entity, not as a public network of cross-linked sibling sites unless strategy explicitly changes later
- keep each market's notes, assets, proofs, routing, and operational context inside that market's own project folder
- do not carry this SOP's brand-separation rules over to unrelated projects unless a different project explicitly adopts them

## What should be standardized vs customized

### Standardize

- site structure
- service stack
- CTA pattern
- schema pattern
- page-type framework
- QA checklist
- design system
- technical deployment flow

### Customize

- brand name
- domain
- phone and email
- city and metro ring
- area pages
- local phrasing
- local proof
- niche examples
- qualification language if needed
- contact routing

## Final QA checklist before any market goes live

- all titles updated
- all meta descriptions updated
- all canonicals updated
- all schema URLs updated
- all phone numbers updated
- all city and state references updated
- all area pages linked properly
- all footer links correct
- sitemap.xml complete
- robots.txt correct
- contact routing tested
- mobile nav tested
- no placeholder proof left behind
- no unsupported claims published

## Definition of done

A market clone is complete when:

- the site can stand on its own in the new market
- the messaging still reflects the integrated growth offer
- the pages feel locally grounded, not mechanically swapped
- the contact path works
- the technical SEO basics are correct
- the site is launch-ready without manual cleanup
