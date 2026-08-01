import fs from 'fs';
import path from 'path';

const OUT = 'c:/autosait/koko-studio/assets/img';
fs.mkdirSync(OUT, { recursive: true });

const data = JSON.parse(fs.readFileSync('c:/autosait/koko-studio/images.json', 'utf8'));
const srcs = [...new Set(data.dom.map((d) => d.src).filter(Boolean))];

// salon photo gallery = get-altay; product cards = get-sprav-products; logo/bg = get-maps-adv-crm
const groups = {
  gallery: srcs.filter((s) => s.includes('/get-altay/')),
  product: srcs.filter((s) => s.includes('/get-sprav-products/')),
  brand: srcs.filter((s) => s.includes('/get-maps-adv-crm/') || s.includes('/get-sprav-posts/')),
};

const sizes = ['orig', 'XXXL', 'XXL', 'XL', 'L'];

async function tryDownload(base, sizesToTry, dest) {
  for (const sz of sizesToTry) {
    const url = base.replace(/\/[^/]+$/, '/' + sz);
    try {
      const res = await fetch(url);
      if (!res.ok) continue;
      const buf = Buffer.from(await res.arrayBuffer());
      if (buf.length < 2000) continue;
      fs.writeFileSync(dest, buf);
      return { url, bytes: buf.length, size: sz };
    } catch {}
  }
  return null;
}

const manifest = [];
for (const [group, list] of Object.entries(groups)) {
  let i = 0;
  for (const src of list) {
    i++;
    const name = `${group}-${String(i).padStart(2, '0')}.jpg`;
    const dest = path.join(OUT, name);
    const r = await tryDownload(src, sizes, dest);
    if (r) {
      manifest.push({ file: name, group, source: src, downloaded: r.url, bytes: r.bytes, size: r.size });
      console.log(name, r.size, r.bytes);
    } else {
      console.log('FAIL', src);
    }
  }
}
fs.writeFileSync('c:/autosait/koko-studio/photo_manifest.json', JSON.stringify(manifest, null, 2));
console.log('total', manifest.length);
