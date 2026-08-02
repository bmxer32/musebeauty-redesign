const fs = require('fs');

const imgs = [
  'noroot.png',
  '294079F4-F2D6-40CD-9.jpeg',
  '4BA72AEE-E5E5-41B0-A.jpeg',
  'image_-1.png',
  'v2_nails_gal_1.jpg',
  'v2_nails_gal_2.jpg',
  'v2_nails_gal_3.jpg',
  'v2_nails_gal_4.jpg',
  'v2_lashes_gal_1.jpg',
  'v2_lashes_gal_2.jpg',
  'v2_brows_gal_1.jpg',
  'v2_brows_gal_2.jpg',
  'v2_brows_gal_3.jpg',
  'v2_brows_gal_4.jpg',
  'v2_hair_gal_1.jpg',
  'v2_hair_gal_3.jpg',
  'v2_hair_gal_4.jpg',
  'v2_luxhair_gal_1.jpg',
  'muse_img_11.jpg',
  'muse_img_12.jpg',
  'muse_img_24.jpg',
  'muse_img_50.jpg',
  'muse_img_70.jpg',
  'muse_img_48.jpg',
  'muse_img_8.jpg',
  '2072743F-D526-49B9-8.jpeg',
  '209E1C9C-5C52-4141-9.jpeg',
  'F09AB9EC-4715-4CE5-8.jpeg',
  '441C87DB-1796-4122-8.jpeg',
  'CFA297DD-A8F4-471D-B.jpeg',
  '9E335A47-6E57-4C87-8.jpeg',
  '2558E8CB-F90B-4B83-A.jpeg',
  '89C75270-F1FD-4357-8.jpeg',
];

let rows = '';
for (const f of imgs) {
  rows += `<div style="display:inline-block;margin:8px;width:200px;vertical-align:top;text-align:center;background:#fff;border-radius:8px;padding:6px">
    <img src="./assets/img/${f}" style="width:100%;height:150px;object-fit:cover;border-radius:4px">
    <div style="font-size:11px;margin-top:4px;word-break:break-all">${f}</div>
  </div>`;
}

const html = `<html><body style="background:#eee;padding:10px">${rows}</body></html>`;
fs.writeFileSync('c:/autosait/audit.html', html);
console.log('audit.html created');
