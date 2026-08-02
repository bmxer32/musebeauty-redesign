import os
import re

# High resolution mapping for each page and section
image_replacements = {
    # Low-res thumbnails replaced by crisp high-res equivalents
    "assets/img/D268D910-FD37-4176-8.jpeg": "assets/img/89C75270-F1FD-4357-8.jpeg",
    "assets/img/A524FF7D-032D-48DC-8.jpeg": "assets/img/209E1C9C-5C52-4141-9.jpeg",
    "assets/img/51FC2374-2DAE-4FDA-9.jpeg": "assets/img/2558E8CB-F90B-4B83-A.jpeg",
    "assets/img/8051AD1C-D084-410A-9.webp": "assets/img/A0C70495-F617-43CF-B.jpeg",
    "assets/img/9D3CEFF2-2D5A-4C16-8.webp": "assets/img/noroot.png",
    "assets/img/AF744DA3-0712-450D-A.webp": "assets/img/image_-1.png"
}

html_files = [f for f in os.listdir('.') if f.endswith('.html') and not f.startswith(('live_', 'raw_', 'yclients_'))]

for fname in html_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update logo image tag width & height
    content = content.replace(
        '<img src="./assets/img/5AA1398A-7545-4FC2-B.png" alt="Muse Beauty Logo" width="120" height="36">',
        '<img src="./assets/img/5AA1398A-7545-4FC2-B.png" alt="Muse Beauty Logo" width="32" height="32">'
    )
    
    # 2. Apply high-res image replacements
    for low_res, high_res in image_replacements.items():
        content = content.replace(low_res, high_res)
        
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated image references and header logo tags across {len(html_files)} HTML pages.")
