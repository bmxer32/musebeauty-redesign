import urllib.request
import os
from PIL import Image
from io import BytesIO

# Replace gal_2 with actual makeup face photo
images = {
    "v3_makeup_gal_2.jpg": "https://images.unsplash.com/photo-1516975080664-ed2fc6a32937?w=800&h=600&fit=crop",
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
