#!/usr/bin/env python3
from pathlib import Path
from textwrap import dedent

root = Path('/data/.openclaw/workspace/projects/soda-city-growth')
areas_dir = root / 'areas'

areas = [
    {
        'slug': 'columbia-sc-marketing-agency.html',
        'city': 'Columbia',
        'title': 'Marketing Agency in Columbia, SC | Websites, SEO, GBP & Ads | Soda City Growth',
        'meta': 'Soda City Growth helps Columbia, SC businesses with free website builds, local SEO, Google Business Profile management, monthly posts, citation support, and Google Ads.',
        'og': 'Free website builds, local SEO, Google Business Profile management, monthly posts, citation support, and Google Ads for Columbia, SC businesses.',
        'hero_h1': 'Get a stronger local presence for your Columbia business, where clearer positioning and better follow-through matter fast.',
        'lead': 'Columbia is the core market, which usually means more comparisons, more noise, and less room for a vague offer. We fix the website first, then support it with local SEO, Google Business Profile management, monthly posts, citation submissions, and paid traffic that lands on the right page and helps turn attention into calls and leads.',
        'sidebar_title': 'What improves in Columbia',
        'sidebar_items': [
            'Service pages that explain the offer faster',
            'Google Business Profile management with monthly posts',
            'Citation support that reinforces local consistency',
            'Landing pages that make ad traffic easier to convert'
        ],
        'card1_title': 'Why Columbia businesses feel pressure faster',
        'card1_text': 'In the core market, prospects compare quickly. If the site feels generic, outdated, or hard to trust, the business has less time to earn the call.',
        'card2_title': 'How the full offer helps',
        'card2_text': 'The website, local SEO, Google Business Profile activity, citation work, and paid traffic all support the same story, so the business feels clearer everywhere someone checks first.',
        'value_title': 'In Columbia, the strongest results usually come when every channel supports the same message.',
        'value_text': 'For qualifying businesses, the free website offer removes the upfront build cost. The real value is what happens after launch: stronger local visibility, a more credible first impression, and better conversion paths across the full growth stack.',
        'feature1_title': 'Stand out faster in the core market',
        'feature1_text': 'Clearer positioning and stronger service pages help the business make sense faster when people compare several local options at once.',
        'feature2_title': 'Stay active across search and maps',
        'feature2_text': 'Google Business Profile management, monthly posts, and citation support help the business show more signs of life where local search often starts.',
        'feature3_title': 'Turn more traffic into real inquiries',
        'feature3_text': 'Paid landing pages and cleaner calls to action make it easier for organic and paid traffic to turn into calls, texts, and leads.',
        'related_title': 'See how the full Columbia offer comes together.',
        'service1_text': 'See how the website offer works and why it is used as the starting point instead of the whole pitch.',
        'service2_text': 'Learn how local SEO, Google Business Profile management, monthly posts, and citations work together.',
        'service3_text': 'See how paid traffic performs better when the message and landing page finally match.'
    },
    {
        'slug': 'lexington-sc-marketing-agency.html',
        'city': 'Lexington',
        'title': 'Marketing Agency in Lexington, SC | Websites, SEO, GBP & Ads | Soda City Growth',
        'meta': 'Soda City Growth helps Lexington, SC businesses with free website builds, local SEO, Google Business Profile management, monthly posts, citation support, and Google Ads.',
        'og': 'Free website builds, local SEO, Google Business Profile management, monthly posts, citation support, and Google Ads for Lexington, SC businesses.',
        'hero_h1': 'Get a clearer local presence for your Lexington business, not just a prettier website.',
        'lead': 'If the offer is solid but the site feels generic, Lexington prospects get less reason to trust the business quickly. We fix the website first, then support it with local SEO, Google Business Profile management, monthly posts, citation submissions, and paid traffic that lands on pages built to match the click.',
        'sidebar_title': 'What improves in Lexington',
        'sidebar_items': [
            'Sharper service pages for Lexington-area searches',
            'Google Business Profile management with regular posting',
            'Citation support that strengthens local trust signals',
            'Landing pages built to turn interest into calls'
        ],
        'card1_title': 'Why Lexington businesses often need clarity first',
        'card1_text': 'A lot of local demand is trust-based. When the site explains the offer faster and feels more current, prospects have a better reason to keep moving toward the call.',
        'card2_title': 'How the full offer helps after launch',
        'card2_text': 'The website becomes the base for local SEO, Google Business Profile management, monthly posts, citation work, and ads, so each channel has a stronger page and message behind it.',
        'value_title': 'The value is not just the build. It is better visibility and better follow-through after launch.',
        'value_text': 'For qualifying Lexington businesses, the free website offer gets the foundation in place first. From there, the real service is the broader local growth stack that keeps visibility active and lead flow stronger over time.',
        'feature1_title': 'Make the offer easier to trust',
        'feature1_text': 'Clear service pages and a stronger first impression help Lexington prospects understand what they are getting without hunting for basic answers.',
        'feature2_title': 'Stay active in local search and maps',
        'feature2_text': 'Google Business Profile management, monthly posts, and citation support help the business look active and consistent where local customers already search.',
        'feature3_title': 'Send paid traffic to stronger pages',
        'feature3_text': 'Landing pages built around the offer give Google Ads clicks a better chance to turn into calls and booked jobs.',
        'related_title': 'See how the full Lexington offer works in practice.',
        'service1_text': 'See how the website offer works and which businesses are usually the best fit for it.',
        'service2_text': 'Learn how local SEO, Google Business Profile activity, and structured content support Lexington visibility.',
        'service3_text': 'See how paid traffic feels more useful when the landing page finally matches the offer.'
    },
    {
        'slug': 'west-columbia-sc-marketing-agency.html',
        'city': 'West Columbia',
        'title': 'Marketing Agency in West Columbia, SC | Websites, SEO, GBP & Ads | Soda City Growth',
        'meta': 'Soda City Growth helps West Columbia, SC businesses with free website builds, local SEO, Google Business Profile management, monthly posts, citation support, and Google Ads.',
        'og': 'Free website builds, local SEO, Google Business Profile management, monthly posts, citation support, and Google Ads for West Columbia, SC businesses.',
        'hero_h1': 'Get a clearer local presence for your West Columbia business before you spend more trying to force attention.',
        'lead': 'Many West Columbia businesses do not need more noise. They need a site that explains the offer faster, a stronger Google Business Profile, and landing pages that give nearby traffic a better place to land. We fix the foundation first, then support it with the full local growth stack.',
        'sidebar_title': 'What improves in West Columbia',
        'sidebar_items': [
            'A clearer offer and stronger first impression',
            'Google Business Profile management with monthly posts',
            'Citation support that strengthens nearby search signals',
            'Paid landing pages that make the next step easier'
        ],
        'card1_title': 'Why West Columbia benefits from sharper positioning',
        'card1_text': 'Businesses here often compete against broader Columbia options. A site that gets to the point faster gives local prospects a better reason to trust the business now instead of later.',
        'card2_title': 'How the full offer supports nearby demand',
        'card2_text': 'The website, local SEO, Google Business Profile activity, citations, and ads all support the same message, so the business feels more established wherever someone checks first.',
        'value_title': 'The website is the starting point. The value is the stronger local system behind it.',
        'value_text': 'For qualifying West Columbia businesses, the free website offer removes the upfront build cost. The ongoing value comes from clearer positioning, steadier local visibility, and better lead flow after launch.',
        'feature1_title': 'Clarify the offer sooner',
        'feature1_text': 'Service pages and homepage messaging can do a better job showing what makes the business worth contacting before the visitor bounces or keeps comparing.',
        'feature2_title': 'Support maps and local search',
        'feature2_text': 'Google Business Profile management, monthly posts, and citation support help the business look more active and more consistent in local discovery.',
        'feature3_title': 'Make ad clicks easier to convert',
        'feature3_text': 'Paid traffic works better when the landing page is aligned to the keyword, the ad, and the actual offer instead of sending everyone to a vague homepage.',
        'related_title': 'See how the full West Columbia offer fits together.',
        'service1_text': 'See why the website comes first and how the free-build model supports the larger service stack.',
        'service2_text': 'Learn how local SEO, Google Business Profile management, and citation work help nearby visibility stay active.',
        'service3_text': 'See how better landing pages help paid traffic feel more relevant from the first click.'
    },
    {
        'slug': 'cayce-sc-marketing-agency.html',
        'city': 'Cayce',
        'title': 'Marketing Agency in Cayce, SC | Websites, SEO, GBP & Ads | Soda City Growth',
        'meta': 'Soda City Growth helps Cayce, SC businesses with free website builds, local SEO, Google Business Profile management, monthly posts, citation support, and Google Ads.',
        'og': 'Free website builds, local SEO, Google Business Profile management, monthly posts, citation support, and Google Ads for Cayce, SC businesses.',
        'hero_h1': 'Get a site and local presence that make it easier for Cayce customers to call instead of keep looking.',
        'lead': 'In a close-in market like Cayce, people often decide quickly from mobile search, maps, and simple comparisons. We fix the website first, then support it with local SEO, Google Business Profile management, monthly posts, citation submissions, and paid traffic that sends people to pages built to convert.',
        'sidebar_title': 'What improves in Cayce',
        'sidebar_items': [
            'A faster first impression on mobile',
            'Google Business Profile management with steady updates',
            'Citation support for stronger local consistency',
            'Landing pages with clearer next steps'
        ],
        'card1_title': 'Why Cayce needs a fast first impression',
        'card1_text': 'When someone is searching nearby, the business usually does not get a long audition. The site has to explain the offer fast and make the next step feel easy.',
        'card2_title': 'How the full offer supports that',
        'card2_text': 'The website, local SEO, Google Business Profile activity, citation work, and ads all work better when the message is clear and the page makes the call or text feel simple.',
        'value_title': 'The value is quicker trust, stronger local signals, and easier next steps after launch.',
        'value_text': 'For qualifying Cayce businesses, the free website offer helps get the foundation live first. The ongoing service then keeps that foundation working harder across search, maps, and paid traffic.',
        'feature1_title': 'Make the site easier to act on',
        'feature1_text': 'Cleaner pages, better calls to action, and a stronger mobile experience make it easier for nearby prospects to turn interest into contact.',
        'feature2_title': 'Stay visible where local searches start',
        'feature2_text': 'Google Business Profile management, monthly posts, and citations help the business look current and more trustworthy in maps and local results.',
        'feature3_title': 'Give paid clicks a better path',
        'feature3_text': 'Landing pages aligned to the ad and service help reduce wasted clicks and make the next step feel more obvious.',
        'related_title': 'See how the full Cayce offer works together.',
        'service1_text': 'See how the website offer supports the bigger goal of better visibility and lead flow after launch.',
        'service2_text': 'Learn how local SEO, Google Business Profile management, and citations reinforce each other in nearby searches.',
        'service3_text': 'See how paid search works better when the landing page makes the next step easy.'
    },
    {
        'slug': 'irmo-sc-marketing-agency.html',
        'city': 'Irmo',
        'title': 'Marketing Agency in Irmo, SC | Websites, SEO, GBP & Ads | Soda City Growth',
        'meta': 'Soda City Growth helps Irmo, SC businesses with free website builds, local SEO, Google Business Profile management, monthly posts, citation support, and Google Ads.',
        'og': 'Free website builds, local SEO, Google Business Profile management, monthly posts, citation support, and Google Ads for Irmo, SC businesses.',
        'hero_h1': 'Get a cleaner, more trustworthy local presence for your Irmo business.',
        'lead': 'A lot of Irmo businesses do not need louder marketing first. They need a clearer offer, stronger service-area pages, a more active Google Business Profile, and landing pages that make the next step easier. We build that system from the website outward.',
        'sidebar_title': 'What improves in Irmo',
        'sidebar_items': [
            'Clearer service-area messaging and page structure',
            'Google Business Profile management with monthly posts',
            'Citation support that reinforces trust signals',
            'Paid landing pages built for stronger conversion'
        ],
        'card1_title': 'Why Irmo businesses often need better service-area clarity',
        'card1_text': 'If the site is vague about what the business does and where it works, both search systems and real people have a harder time trusting the next step.',
        'card2_title': 'How the full offer helps after launch',
        'card2_text': 'The website becomes the base for local SEO, Google Business Profile management, monthly posts, citations, and ads, so the business stays clearer and more active everywhere people look.',
        'value_title': 'Irmo growth usually gets easier when the offer and service area are obvious.',
        'value_text': 'For qualifying Irmo businesses, the free website offer gets the foundation live without upfront build cost. The ongoing value comes from stronger local clarity, steadier visibility, and better lead flow across the full stack.',
        'feature1_title': 'Clarify what you do and where you work',
        'feature1_text': 'Service pages, location context, and cleaner navigation help the business make sense faster to both visitors and search systems.',
        'feature2_title': 'Stay active in local discovery',
        'feature2_text': 'Google Business Profile management, monthly posts, and citation work help the business look more current and more trustworthy in local search.',
        'feature3_title': 'Support stronger conversion paths',
        'feature3_text': 'Landing pages and better calls to action help both organic and paid traffic turn into calls, texts, and real inquiries.',
        'related_title': 'See how the full Irmo offer comes together.',
        'service1_text': 'See why the website is used as the foundation for the broader local growth system.',
        'service2_text': 'Learn how local SEO, Google Business Profile activity, and citation support help Irmo visibility stay active.',
        'service3_text': 'See how stronger landing pages give paid traffic a clearer path to convert.'
    },
    {
        'slug': 'forest-acres-sc-marketing-agency.html',
        'city': 'Forest Acres',
        'title': 'Marketing Agency in Forest Acres, SC | Websites, SEO, GBP & Ads | Soda City Growth',
        'meta': 'Soda City Growth helps Forest Acres, SC businesses with free website builds, local SEO, Google Business Profile management, monthly posts, citation support, and Google Ads.',
        'og': 'Free website builds, local SEO, Google Business Profile management, monthly posts, citation support, and Google Ads for Forest Acres, SC businesses.',
        'hero_h1': 'Get a more polished local presence for your Forest Acres business, with a clearer offer and stronger trust from the first visit.',
        'lead': 'In a market where presentation and credibility matter, a vague or dated site can quietly work against the business. We fix the website first, then support it with local SEO, Google Business Profile management, monthly posts, citation submissions, and paid traffic that lands on pages built to feel more credible and clear.',
        'sidebar_title': 'What improves in Forest Acres',
        'sidebar_items': [
            'A more polished first impression',
            'Google Business Profile management with regular posting',
            'Citation support that reinforces consistency',
            'Landing pages that feel cleaner and more trustworthy'
        ],
        'card1_title': 'Why Forest Acres businesses benefit from a stronger first impression',
        'card1_text': 'When people notice the details, the business needs a site that feels current, well-structured, and easier to trust before they ever reach out.',
        'card2_title': 'How the offer supports ongoing visibility',
        'card2_text': 'The website, local SEO, Google Business Profile activity, citation work, and ads all reinforce the same message, so the business looks more established everywhere someone checks first.',
        'value_title': 'The full offer helps you look more established wherever people compare options.',
        'value_text': 'For qualifying Forest Acres businesses, the free website offer gets the foundation in better shape first. The broader service stack then supports stronger local visibility, a more credible brand impression, and better lead flow after launch.',
        'feature1_title': 'Sharpen the first impression',
        'feature1_text': 'Cleaner messaging, page structure, and design help the business feel more credible and easier to trust from the first visit.',
        'feature2_title': 'Support local visibility with consistency',
        'feature2_text': 'Google Business Profile management, monthly posts, and citations help the business stay active and aligned across the places people check most.',
        'feature3_title': 'Give traffic a more credible landing page',
        'feature3_text': 'Whether traffic comes from search or ads, stronger landing pages make the next step feel clearer and more comfortable.',
        'related_title': 'See how the full Forest Acres offer fits together.',
        'service1_text': 'See how the website offer helps establish a stronger foundation before the ongoing work begins.',
        'service2_text': 'Learn how local SEO, Google Business Profile management, and citation support strengthen search visibility.',
        'service3_text': 'See how paid search works better when the landing page feels credible and aligned to the offer.'
    }
]

template = """<!doctype html>
<html lang=\"en-US\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>{title}</title>
  <meta name=\"description\" content=\"{meta}\" />
  <meta name=\"robots\" content=\"index,follow\" />
  <meta property=\"og:title\" content=\"{title}\" />
  <meta property=\"og:description\" content=\"{og}\" />
  <meta property=\"og:type\" content=\"article\" />
  <meta property=\"og:url\" content=\"https://sodacitygrowth.com/areas/{slug}\" />
  <link rel=\"canonical\" href=\"https://sodacitygrowth.com/areas/{slug}\" />
  <link rel=\"icon\" href=\"/favicon.svg\" type=\"image/svg+xml\" />
  <link rel=\"stylesheet\" href=\"/styles.css\" />
  <script type=\"application/ld+json\">
  {{
    \"@context\": \"https://schema.org\",
    \"@graph\": [
      {{
        \"@type\": \"Service\",
        \"@id\": \"https://sodacitygrowth.com/areas/{slug}#service\",
        \"name\": \"Marketing services in {city}, South Carolina\",
        \"serviceType\": [\"Website design\", \"Local SEO\", \"Google Business Profile management\", \"Google Ads\"],
        \"url\": \"https://sodacitygrowth.com/areas/{slug}\",
        \"description\": \"{meta}\",
        \"provider\": {{
          \"@id\": \"https://sodacitygrowth.com/#localbusiness\"
        }},
        \"areaServed\": \"{city}, South Carolina\"
      }},
      {{
        \"@type\": \"LocalBusiness\",
        \"@id\": \"https://sodacitygrowth.com/#localbusiness\",
        \"name\": \"Soda City Growth\",
        \"url\": \"https://sodacitygrowth.com/\",
        \"description\": \"Soda City Growth is a Columbia, South Carolina marketing website focused on free website builds for qualifying businesses, local SEO, Google Business Profile management, citation support, AI-ready page structure, and Google Ads landing pages.\",
        \"telephone\": \"+1-803-602-4458\",
        \"logo\": {{
          \"@type\": \"ImageObject\",
          \"url\": \"https://sodacitygrowth.com/assets/branding/soda-city-growth-logo.webp\"
        }},
        \"image\": \"https://sodacitygrowth.com/assets/branding/soda-city-growth-logo.webp\",
        \"serviceArea\": [
          \"Columbia, South Carolina\",
          \"Lexington, South Carolina\",
          \"West Columbia, South Carolina\",
          \"Cayce, South Carolina\",
          \"Irmo, South Carolina\",
          \"Forest Acres, South Carolina\"
        ],
        \"areaServed\": [
          \"Columbia, South Carolina\",
          \"Lexington, South Carolina\",
          \"West Columbia, South Carolina\",
          \"Cayce, South Carolina\",
          \"Irmo, South Carolina\",
          \"Forest Acres, South Carolina\"
        ]
      }},
      {{
        \"@type\": \"WebPage\",
        \"@id\": \"https://sodacitygrowth.com/areas/{slug}#webpage\",
        \"url\": \"https://sodacitygrowth.com/areas/{slug}\",
        \"name\": \"{title}\",
        \"description\": \"{meta}\",
        \"mainEntity\": {{
          \"@id\": \"https://sodacitygrowth.com/areas/{slug}#service\"
        }},
        \"about\": {{
          \"@id\": \"https://sodacitygrowth.com/#localbusiness\"
        }},
        \"inLanguage\": \"en-US\"
      }},
      {{
        \"@type\": \"BreadcrumbList\",
        \"@id\": \"https://sodacitygrowth.com/areas/{slug}#breadcrumb\",
        \"itemListElement\": [
          {{
            \"@type\": \"ListItem\",
            \"position\": 1,
            \"name\": \"Home\",
            \"item\": \"https://sodacitygrowth.com/\"
          }},
          {{
            \"@type\": \"ListItem\",
            \"position\": 2,
            \"name\": \"Marketing Agency in {city}, SC\",
            \"item\": \"https://sodacitygrowth.com/areas/{slug}\"
          }}
        ]
      }}
    ]
  }}
  </script>
</head>
<body>
  <header class=\"site-header\">
    <div class=\"wrap header-row\">
      <a class=\"brand\" href=\"/\">
        <span class=\"brand-mark\">SC</span>
        <span>
          <strong>Soda City Growth</strong>
          <small>Columbia, SC websites, SEO and paid ads</small>
        </span>
      </a>
      <button class=\"nav-toggle\" aria-expanded=\"false\" aria-controls=\"site-nav\">Menu</button>
      <nav class=\"nav\" id=\"site-nav\">
        <a href=\"/\">Home</a>
        <a href=\"/services/free-websites-columbia-sc\">Free Websites</a>
        <a href=\"/services/seo-ai-ranking-columbia-sc\">SEO + AI</a>
        <a href=\"/services/google-ads-columbia-sc\">Paid Ads</a>
        <a href=\"/contact\">Contact</a>
        <a class=\"nav-phone\" href=\"tel:+18036024458\">Call Now</a>
      </nav>
    </div>
  </header>

  <main class=\"inner-page\">
    <section class=\"page-hero\">
      <div class=\"wrap split-section\">
        <div>
          <p class=\"eyebrow\">Marketing agency in {city}, SC</p>
          <h1>{hero_h1}</h1>
          <p class=\"lead\">{lead}</p>
          <div class=\"hero-actions\">
            <a class=\"button\" href=\"tel:+18036024458\">Call Now</a>
            <a class=\"button secondary\" href=\"/services/free-websites-columbia-sc\">See the website offer</a>
          </div>
        </div>
        <aside class=\"sidebar-card\">
          <h2>{sidebar_title}</h2>
          <ul class=\"bullet-list\">
            <li>{sidebar_items[0]}</li>
            <li>{sidebar_items[1]}</li>
            <li>{sidebar_items[2]}</li>
            <li>{sidebar_items[3]}</li>
          </ul>
        </aside>
      </div>
    </section>

    <section class=\"section\">
      <div class=\"wrap card-grid two-up\">
        <article class=\"feature-card\">
          <h2>{card1_title}</h2>
          <p>{card1_text}</p>
        </article>
        <article class=\"feature-card\">
          <h2>{card2_title}</h2>
          <p>{card2_text}</p>
        </article>
      </div>
    </section>

    <section class=\"section muted-section\">
      <div class=\"wrap\">
        <div class=\"section-intro narrow\">
          <p class=\"eyebrow\">What you get in {city}</p>
          <h2>{value_title}</h2>
          <p>{value_text}</p>
        </div>
        <div class=\"card-grid three-up\">
          <article class=\"feature-card\">
            <h3>{feature1_title}</h3>
            <p>{feature1_text}</p>
          </article>
          <article class=\"feature-card\">
            <h3>{feature2_title}</h3>
            <p>{feature2_text}</p>
          </article>
          <article class=\"feature-card\">
            <h3>{feature3_title}</h3>
            <p>{feature3_text}</p>
          </article>
        </div>
      </div>
    </section>

    <section class=\"section\">
      <div class=\"wrap\">
        <div class=\"section-intro narrow\">
          <p class=\"eyebrow\">Related services</p>
          <h2>{related_title}</h2>
        </div>
        <div class=\"service-links\">
          <a class=\"service-link-card\" href=\"/services/free-websites-columbia-sc\">
            <h3>Free Website Builds</h3>
            <p>{service1_text}</p>
            <span>Read more</span>
          </a>
          <a class=\"service-link-card\" href=\"/services/seo-ai-ranking-columbia-sc\">
            <h3>Local SEO + GBP + AI Visibility</h3>
            <p>{service2_text}</p>
            <span>Read more</span>
          </a>
          <a class=\"service-link-card\" href=\"/services/google-ads-columbia-sc\">
            <h3>Google Ads</h3>
            <p>{service3_text}</p>
            <span>Read more</span>
          </a>
        </div>
      </div>
    </section>
  </main>

  <footer class=\"site-footer\">
    <div class=\"wrap footer-row\">
      <div>
        <strong>Soda City Growth</strong>
        <p>Free website builds, local SEO, Google Business Profile management, citation support, and Google Ads for Columbia-area businesses.</p>
        <a class=\"contact-link\" href=\"tel:+18036024458\">Call or text (803) 602-4458</a>
      </div>
      <div class=\"footer-links\">
        <a href=\"/\">Home</a>
        <a href=\"/services/free-websites-columbia-sc\">Free Websites</a>
        <a href=\"/services/seo-ai-ranking-columbia-sc\">SEO + AI</a>
        <a href=\"/services/google-ads-columbia-sc\">Paid Ads</a>
        <a href=\"/contact\">Contact</a>
      </div>
    </div>
  </footer>
  <script src=\"/app.js\"></script>
</body>
</html>
"""

for area in areas:
    (areas_dir / area['slug']).write_text(template.format(**area))

print(f'wrote {len(areas)} area pages')
