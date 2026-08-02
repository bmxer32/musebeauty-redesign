const fs = require('fs');
const imgs = ['v3_makeup_gal_1.jpg', 'v3_makeup_gal_2.jpg', 'v3_makeup_gal_3.jpg', 'v3_makeup_gal_4.jpg'];
let rows = '';
for (const f of imgs) {
  rows += `<div style="display:inline-block;margin:8px;width:300px;vertical-align:top;text-align:center;background:#fff;border-radius:8px;padding:6px">
    <img src="./assets/img/${f}" style="width:100%;height:220px;object-fit:cover;border-radius:4px">
    <div style="font-size:12px;margin-top:4px">${f}</div>
  </div>`;
}
const html = `<html><body style="background:#eee;padding:10px">${rows}</body></html>`;
fs.writeFileSync('c:/autosait/audit_makeup.html', html);
console.log('OK');
