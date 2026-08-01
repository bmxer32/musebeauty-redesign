import urllib.request
import os
from PIL import Image
from io import BytesIO

images = {
    "v3_makeup_gal_1.jpg": "https://images.unsplash.com/photo-1487412912498-0447578fcca8?w=800&h=600&fit=crop",
    "v3_makeup_gal_2.jpg": "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?w=800&h=600&fit=crop",
    "v3_makeup_gal_3.jpg": "https://images.unsplash.com/photo-1512496015851-a90fb38ba796?w=800&h=600&fit=crop",
    "v3_makeup_gal_4.jpg": "https://images.unsplash.com/photo-1457972729786-0411a3b2b626?w=800&h=600&fit=crop",
}

for filename, url in images.items():
    print(f"Downloading {filename}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as response:
            img_data = response.read()
        img = Image.open(BytesIO(img_data))
        if img.mode != 'RGB':
            img = img.convert('RGB')
        width, height = img.size
        target_ratio = 4/3
        current_ratio = width / height
        if current_ratio > target_ratio:
            new_width = int(height * target_ratio)
            left = (width - new_width) / 2
            img = img.crop((left, 0, left + new_width, height))
        else:
            new_height = int(width / target_ratio)
            top = (height - new_height) / 2
            img = img.crop((0, top, width, top + new_height))
        img = img.resize((800, 600), Image.Resampling.LANCZOS)
        img.save(os.path.join("assets/img", filename), "JPEG", quality=85)
        print(f"OK: {filename}")
    except Exception as e:
        print(f"FAIL: {filename}: {e}")
