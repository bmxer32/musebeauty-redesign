import os
from PIL import Image

imgs = [f for f in os.listdir('assets/img') if f.endswith(('.jpg', '.jpeg', '.png', '.webp'))]

html_lines = [
    "<!DOCTYPE html>",
    "<html><head><meta charset='utf-8'><title>Image Inventory</title>",
    "<style>body{font-family:sans-serif;background:#222;color:#fff;padding:20px;}",
    ".grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:16px;}",
    ".card{background:#333;padding:10px;border-radius:8px;text-align:center;}",
    ".card img{max-width:100%;height:150px;object-fit:cover;border-radius:4px;}",
    ".info{font-size:12px;margin-top:6px;word-break:break-all;}",
    "</style></head><body>",
    f"<h1>All {len(imgs)} Downloaded Local Images</h1>",
    "<div class='grid'>"
]

for fname in sorted(imgs):
    path = os.path.join('assets/img', fname)
    try:
        with Image.open(path) as img:
            w, h = img.size
            html_lines.append(f"""
            <div class='card'>
              <img src='assets/img/{fname}' alt='{fname}'>
              <div class='info'>
                <strong>{fname}</strong><br>
                {w}x{h} px | {round(os.path.getsize(path)/1024, 1)} KB
              </div>
            </div>
            """)
    except Exception as e:
        pass

html_lines.append("div></body></html>")

with open('gallery_index.html', 'w', encoding='utf-8') as f:
    f.write("\n".join(html_lines))

print("gallery_index.html successfully generated!")
