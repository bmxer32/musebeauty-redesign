import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const projectRoot = __dirname;
let errorCount = 0;

console.log('=== RUNNING STATIC LINK & ASSET VALIDATION CHECK ===\n');

// Only check project site pages, ignore temporary scraped raw html files
const htmlFiles = fs.readdirSync(projectRoot).filter(file => 
  file.endsWith('.html') && !file.includes('live_') && !file.includes('raw_') && !file.includes('_raw')
);

htmlFiles.forEach(file => {
  const filePath = path.join(projectRoot, file);
  const content = fs.readFileSync(filePath, 'utf-8');

  console.log(`Checking ${file}...`);

  // 1. Check for absolute path references (/assets/...)
  const absMatches = content.match(/href=["']\/assets\/[^"']*["']|src=["']\/assets\/[^"']*["']/g);
  if (absMatches) {
    console.error(`  ❌ ERROR in ${file}: Absolute path detected: ${absMatches.join(', ')}`);
    errorCount += absMatches.length;
  }

  // 2. Check relative hrefs and src links
  const matches = [...content.matchAll(/(?:href|src)=["']([^"']+)["']/g)];

  matches.forEach(match => {
    const link = match[1];
    if (link.startsWith('http://') || link.startsWith('https://') || link.startsWith('tel:') || link.startsWith('mailto:') || link.startsWith('#') || link.startsWith('javascript:')) {
      return;
    }

    const resolvedPath = path.resolve(projectRoot, link);
    if (!fs.existsSync(resolvedPath)) {
      console.error(`  ❌ ERROR in ${file}: Broken local path reference "${link}" -> resolved to "${resolvedPath}"`);
      errorCount++;
    }
  });
});

console.log(`\n========================================`);
if (errorCount === 0) {
  console.log(`✅ node check.mjs ........ PASS (0 errors across ${htmlFiles.length} site HTML pages)`);
  process.exit(0);
} else {
  console.error(`❌ node check.mjs ........ FAIL (${errorCount} errors found)`);
  process.exit(1);
}
