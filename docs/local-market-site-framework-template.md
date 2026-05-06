# Local Market Site Framework Template

Use this as the reusable build brief for every new city or metro launch.

## 1. Core project tokens

Fill these first.

- [BRAND_NAME]
- [DOMAIN]
- [PRIMARY_CITY]
- [STATE_NAME]
- [STATE_ABBR]
- [PRIMARY_METRO_LABEL]
- [PHONE_DISPLAY]
- [PHONE_E164]
- [PUBLIC_EMAIL]
- [PRIMARY_CTA]
- [SECONDARY_CTA]
- [CLIENT_CAP]
- [CONTRACT_TERM]
- [FREE_BUILD_RULE]
- [BOOKING_OR_FORM_ROUTE]

## 2. Market footprint

### Primary city

- [PRIMARY_CITY], [STATE_ABBR]

### Secondary service areas

- [AREA_1]
- [AREA_2]
- [AREA_3]
- [AREA_4]
- [AREA_5]
- [AREA_6]
- [AREA_7]
- [AREA_8]

### Local context notes

Capture:

- important neighboring towns
- how people describe the area locally
- whether the market is suburban, urban, commuter-heavy, affluent, blue-collar, mixed, etc.
- trust factors that matter in that market
- search-intent patterns that seem obvious

## 3. Offer stack for the market

Confirm which of these are active:

- free website build for qualifying businesses
- six-month growth partnership
- web design
- local SEO
- Google Business Profile management
- monthly Google Business Profile posts
- citation support
- Google Ads / paid search
- AI-ready SEO structure

## 4. Positioning rules

### Primary positioning statement

Template:

[BRAND_NAME] helps [PRIMARY_CITY]-area businesses get a stronger local presence by fixing the website first, then supporting it with local SEO, Google Business Profile management, citations, and paid traffic.

### Core outcome promises

Use 3 to 5:

- clearer first impression
- stronger local visibility
- better conversion paths
- better lead flow
- faster, more direct support

### Key strategic truths

- the website is the foundation
- the free build is not the whole offer
- ongoing growth work is the main value after launch
- the contract exists because of the upfront research and planning work
- the roster cap exists to support service quality

## 5. Standard sitemap

Build these pages first.

- `/index.html`
- `/contact.html`
- `/services/free-websites-[primary-city]-[state].html`
- `/services/web-design-[primary-city]-[state].html`
- `/services/seo-ai-ranking-[primary-city]-[state].html`
- `/services/google-ads-[primary-city]-[state].html`
- `/areas/[primary-city]-[state]-marketing-agency.html`
- `/areas/[area-2]-[state]-marketing-agency.html`
- `/areas/[area-3]-[state]-marketing-agency.html`
- `/areas/[area-4]-[state]-marketing-agency.html`
- `/areas/[area-5]-[state]-marketing-agency.html`

Add more area pages only if they are commercially relevant.

## 6. Homepage framework

### SEO fields

Title pattern:

[PRIMARY_CITY], [STATE_ABBR] Web Design, SEO & Google Ads | Free Website Builds | [BRAND_NAME]

Description pattern:

[BRAND_NAME] helps [PRIMARY_CITY], [STATE_ABBR] businesses with free website builds, local SEO, Google Business Profile management, citation support, and Google Ads built to earn better leads.

### Homepage section stack

1. Hero
   - outcome-led headline
   - service stack in plain English
   - primary CTA
   - secondary CTA
   - 3 short benefit points

2. Areas served strip
   - primary city
   - 4 to 8 adjacent cities

3. What you get section
   - trust
   - visibility
   - lead flow

4. Qualification / value checklist
   - what improves after launch

5. Differentiators
   - small roster
   - one integrated strategy stack

6. How visibility improves
   - offer clarity
   - page-to-intent matching
   - trust signals
   - ongoing growth work

7. Core services cards
   - free websites
   - SEO + GBP + AI visibility
   - Google Ads

8. Service areas cards
   - one card per major city page

9. Contact CTA block

10. FAQ block

### Homepage schema

Include:

- Organization
- WebSite
- WebPage
- FAQPage

## 7. Service page frameworks

### Free website page

Must answer:

- what the offer is
- who qualifies
- why the build is free
- why it is tied to [CONTRACT_TERM]
- what happens after launch
- why the client cap matters

Sections:

- hero
- best-fit businesses sidebar
- why the offer exists
- what qualifies
- why the contract and cap exist
- FAQ

Schema:

- Service
- WebPage
- BreadcrumbList
- FAQPage

### Web design page

Must answer:

- what the build includes
- why the site comes first
- how it helps SEO
- how it helps paid traffic

Sections:

- hero
- what the build includes
- why the site comes first
- built to support growth
- FAQ

Schema:

- Service
- WebPage
- BreadcrumbList
- FAQPage

### SEO + GBP + AI visibility page

Must answer:

- what local visibility includes
- how Google Business Profile support fits in
- how monthly posts and citations fit in
- what AI-ready means in plain English
- how schema should be used honestly

Sections:

- hero
- what local visibility includes
- how we approach it
- market coverage
- FAQ

Schema:

- Service
- WebPage
- BreadcrumbList
- FAQPage

### Google Ads page

Must answer:

- why landing pages matter
- why page and ad should be aligned
- why the website and ads are linked
- how ads and SEO can reinforce each other

Sections:

- hero
- what we align
- why we pair ads with the site
- local coverage
- FAQ

Schema:

- Service
- WebPage
- BreadcrumbList
- FAQPage

## 8. Area page framework

Each area page needs a specific angle.

### Title pattern

Marketing Agency in [AREA], [STATE_ABBR] | Websites, SEO, GBP & Ads | [BRAND_NAME]

### Description pattern

[BRAND_NAME] helps [AREA], [STATE_ABBR] businesses with free website builds, local SEO, Google Business Profile management, monthly posts, citation support, and Google Ads.

### Required sections

- hero with city-specific angle
- what improves in that city
- why local businesses there often need clarity / trust / stronger conversion pages
- how the full offer helps after launch
- related service links

### Area-page writing rule

Do not mass-produce near-duplicates. Each page should answer:

- what is different about this local market
- what type of buyer behavior matters here
- what trust issue or visibility issue is most relevant here

### Area-page schema

Include:

- Service or WebPage
- BreadcrumbList if used
- areaServed set to that city or market

## 9. Contact page framework

### SEO fields

Title pattern:

Contact [BRAND_NAME] | [PRIMARY_CITY], [STATE_ABBR]

Description pattern:

Contact [BRAND_NAME] in [PRIMARY_CITY], [STATE_NAME]. Call or text [PHONE_DISPLAY], or use the contact form to ask about websites, local SEO, Google Business Profile management, and Google Ads.

### Required sections

- page hero
- quick contact instructions
- direct call/text CTA
- lead form
- alternative direct-contact block

### Lead form fields

- name
- phone
- email
- business
- service interest
- message

### Current fallback routing logic

If there is no backend yet:

- capture the form fields
- open a prefilled SMS draft to [PHONE_E164]

If a backend exists later:

- send form to CRM or inbox
- keep direct call/text option visible

## 10. Content rules

### Always include

- real city and state references
- plain-English explanations
- CTA buttons in hero and footer
- outcome-focused framing
- internal links between services and area pages
- FAQ sections where useful

### Never include unless verified

- public address
- ratings or reviews
- case study outcomes
- certifications
- team size
- years in business
- public email address

## 11. Design system carryover

Keep these unless the brand changes them intentionally:

- warm, local, approachable visual tone
- clean serif + sans pairing
- soft gradients / editorial polish
- sticky nav
- high-contrast CTA button
- simple card-based sections
- mobile-first spacing

## 12. Technical checklist

Before launch, confirm:

- all page titles updated
- all descriptions updated
- all canonical URLs updated
- all schema URLs updated
- all phone links updated
- all email links updated
- sitemap.xml includes all pages
- robots.txt points to the correct sitemap
- footer links are correct
- nav links are correct
- no placeholder market tokens remain
- no old city references remain
- no old domain references remain

## 13. Reusable launch checklist

### Pre-build

- confirm market
- confirm domain
- confirm phone
- confirm offer rules
- confirm service areas

### Build

- duplicate starter
- replace tokens
- rewrite homepage
- rewrite service pages
- rewrite area pages
- update contact page
- update schema
- update sitemap and robots

### QA

- mobile review
- link review
- CTA review
- metadata review
- schema review
- typo review
- market-specific wording review

### Launch

- deploy
- test live pages
- test calls/texts/forms
- submit sitemap if needed

## 14. Suggested future improvements to the framework

Add these later to strengthen every future market launch:

- testimonials module
- case study module
- booking integration
- CRM lead capture
- niche-specific service variants
- stronger local proof blocks
- market-specific FAQ expansions
- reusable content tokens file for programmatic cloning
