import os
from PIL import Image

imgs = [f for f in os.listdir('assets/img') if f.endswith(('.jpg', '.jpeg', '.png', '.webp'))]

print(f"Total image files in assets/img: {len(imgs)}\n")

for fname in sorted(imgs):
    path = os.path.join('assets/img', fname)
    try:
        with Image.open(path) as img:
            w, h = img.size
            print(f"{fname}: {w}x{h} px, format={img.format}, filesize={os.path.getsize(path)} bytes")
    except Exception as e:
        print(f"{fname}: ERROR {e}")
