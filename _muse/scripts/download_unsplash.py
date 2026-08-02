import urllib.request
import os
from PIL import Image
from io import BytesIO

# Using Unsplash Source API for topic-specific images
images = {
    "v3_nails_gal_3.jpg": "https://images.unsplash.com/photo-1604654894610-df63bc536371?w=800&h=600&fit=crop",
    "v3_nails_gal_4.jpg": "https://images.unsplash.com/photo-1632345031435-8727f6897d53?w=800&h=600&fit=crop",
    "v3_main_interior_1.jpg": "https://images.unsplash.com/photo-1560066984-138dadb4c035?w=800&h=600&fit=crop",
    "v3_main_interior_2.jpg": "https://images.unsplash.com/photo-1521590832167-7228b5ea5fa3?w=800&h=600&fit=crop",
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

        # Crop to 4:3
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
        print(f"OK: {filename} ({img.size})")
    except Exception as e:
        print(f"FAIL: {filename}: {e}")
