import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const pages = ['index.html', 'lashes-brows.html', 'hair-salon.html', 'nails-makeup.html'];
let errors = [];

console.log(`Checking ${pages.length} project HTML files: ${pages.join(', ')}...\n`);

pages.forEach(file => {
  const filePath = path.join(__dirname, file);
  if (!fs.existsSync(filePath)) {
    errors.push(`File missing: ${file}`);
    return;
  }

  const content = fs.readFileSync(filePath, 'utf-8');

  // Check CSS linked
  if (!content.includes('./assets/css/style.css')) {
    errors.push(`${file}: Missing ./assets/css/style.css link`);
  }

  // Check JS linked
  if (!content.includes('./assets/js/app.js')) {
    errors.push(`${file}: Missing ./assets/js/app.js script`);
  }

  // Check local images exist
  const imgMatches = content.match(/src=["'](\.\/assets\/img\/[^"']+)["']/g) || [];
  imgMatches.forEach(match => {
    const relativePath = match.replace(/src=["']/, '').replace(/["']$/, '');
    const fullPath = path.join(__dirname, relativePath);
    if (!fs.existsSync(fullPath)) {
      errors.push(`${file}: Local image broken reference -> ${relativePath}`);
    }
  });

  // Check anchor targets
  const anchorMatches = content.match(/href=["'](\.\/[^"']*#[^"']+)["']/g) || [];
  anchorMatches.forEach(match => {
    const rawHref = match.replace(/href=["']/, '').replace(/["']$/, '');
    const [targetFile, anchorId] = rawHref.split('#');
    const targetFilePath = path.join(__dirname, targetFile.replace('./', ''));
    if (fs.existsSync(targetFilePath)) {
      const targetContent = fs.readFileSync(targetFilePath, 'utf-8');
      if (!targetContent.includes(`id="${anchorId}"`)) {
        errors.push(`${file}: Anchor #${anchorId} not found in ${targetFile}`);
      }
    } else {
      errors.push(`${file}: Anchor target file missing -> ${targetFile}`);
    }
  });
});

console.log('--- CHECK RESULTS ---');
if (errors.length === 0) {
  console.log(`PASS: 0 errors in ${pages.length} project HTML files.\n`);
  process.exit(0);
} else {
  console.log(`FAIL: Found ${errors.length} errors:`);
  errors.forEach(err => console.error(` - ${err}`));
  process.exit(1);
}
