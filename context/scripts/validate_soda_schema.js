const fs = require('fs');
const path = require('path');
const files = [
  'index.html',
  'services/free-websites-columbia-sc.html',
  'services/web-design-columbia-sc.html',
  'services/seo-ai-ranking-columbia-sc.html',
  'services/google-ads-columbia-sc.html',
  'areas/lexington-sc-marketing-agency.html',
  'areas/west-columbia-sc-marketing-agency.html',
  'areas/irmo-sc-marketing-agency.html'
];
const root = '/data/.openclaw/workspace/projects/soda-city-growth';
for (const rel of files) {
  const html = fs.readFileSync(path.join(root, rel), 'utf8');
  const matches = [...html.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g)];
  for (const [i, match] of matches.entries()) {
    try {
      JSON.parse(match[1]);
    } catch (err) {
      console.error(`SCHEMA_PARSE_ERROR ${rel} block ${i + 1}: ${err.message}`);
      process.exit(1);
    }
  }
}
console.log('SCHEMA_JSON_OK');
