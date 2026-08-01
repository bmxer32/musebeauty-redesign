const fs = require('fs');
const imgs = ['v3_nails_gal_3.jpg', 'v3_nails_gal_4.jpg', 'v3_main_interior_1.jpg', 'v3_main_interior_2.jpg'];
let rows = '';
for (const f of imgs) {
  rows += `<div style="display:inline-block;margin:8px;width:300px;vertical-align:top;text-align:center;background:#fff;border-radius:8px;padding:6px">
    <img src="./assets/img/${f}" style="width:100%;height:220px;object-fit:cover;border-radius:4px">
    <div style="font-size:12px;margin-top:4px">${f}</div>
  </div>`;
}
const html = `<html><body style="background:#eee;padding:10px">${rows}</body></html>`;
fs.writeFileSync('c:/autosait/audit3.html', html);
console.log('audit3.html created');
