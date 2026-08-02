const fs = require('fs');

// All remaining muse_img files not yet audited
const imgs = [
  'muse_img_11.jpg', 'muse_img_12.jpg', 'muse_img_14.jpg',
  'muse_img_19.jpg', 'muse_img_2.jpg', 'muse_img_21.jpg',
  'muse_img_23.jpg', 'muse_img_24.jpg', 'muse_img_25.jpg',
  'muse_img_30.jpg', 'muse_img_32.jpg', 'muse_img_36.jpg',
  'muse_img_37.jpg', 'muse_img_40.jpg', 'muse_img_43.jpg',
  'muse_img_44.jpg', 'muse_img_45.jpg', 'muse_img_47.jpg',
  'muse_img_48.jpg', 'muse_img_50.jpg', 'muse_img_52.jpg',
  'muse_img_53.jpg', 'muse_img_54.jpg', 'muse_img_58.jpg',
  'muse_img_62.jpg', 'muse_img_64.jpg', 'muse_img_70.jpg',
  'muse_img_73.jpg', 'muse_img_76.jpg', 'muse_img_8.jpg',
  '24E4ADBA-B26A-422E-9.jpeg',
  '9A549102-7AC4-4C4C-B.jpeg',
  'A524FF7D-032D-48DC-8.jpeg',
  'D268D910-FD37-4176-8.jpeg',
  'F8464A9E-67AB-44E3-B.jpeg',
  'generated.jpg',
];

let rows = '';
for (const f of imgs) {
  rows += `<div style="display:inline-block;margin:8px;width:200px;vertical-align:top;text-align:center;background:#fff;border-radius:8px;padding:6px">
    <img src="./assets/img/${f}" style="width:100%;height:150px;object-fit:cover;border-radius:4px" onerror="this.style.background='#f88';this.alt='MISSING'">
    <div style="font-size:11px;margin-top:4px;word-break:break-all">${f}</div>
  </div>`;
}

const html = `<html><body style="background:#eee;padding:10px">${rows}</body></html>`;
fs.writeFileSync('c:/autosait/audit2.html', html);
console.log('audit2.html created');
