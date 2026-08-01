const fs = require('fs');
const files = ['24E4ADBA-B26A-422E-9.jpeg', 'A0C70495-F617-43CF-B.jpeg', '5AF19170-D201-432E-B.jpeg', '51FC2374-2DAE-4FDA-9.jpeg', 'CF9B0EE0-51FE-4E0A-A.webp', '3B52DDCC-3A98-424D-B.webp', 'F8464A9E-67AB-44E3-B.jpeg', 'CCB92D88-733F-4D50-9.webp', '2558E8CB-F90B-4B83-A.jpeg', '89C75270-F1FD-4357-8.jpeg', '209E1C9C-5C52-4141-9.jpeg', '67F00D5B-3A34-4337-A.jpeg', 'F09AB9EC-4715-4CE5-8.jpeg', '441C87DB-1796-4122-8.jpeg', 'CFA297DD-A8F4-471D-B.jpeg', '9E335A47-6E57-4C87-8.jpeg', 'muse_img_52.jpg', 'muse_img_36.jpg', 'muse_img_37.jpg'];
let html = '<html><body style=\"display:flex;flex-wrap:wrap;\">';
for (let f of files) {
  html += '<div style=\"margin:5px;text-align:center;width:250px;\"><img src=\"./assets/img/' + f + '\" style=\"width:100%;height:200px;object-fit:cover;\"><br><span style=\"font-size:12px\">' + f + '</span></div>';
}
html += '</body></html>';
fs.writeFileSync('c:/autosait/preview.html', html);
console.log('preview.html generated');
