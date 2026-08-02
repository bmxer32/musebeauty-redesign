import urllib.request
import urllib.parse
import json
import os
from PIL import Image
from io import BytesIO

queries = {
    "v2_nails_gal_3.jpg": "manicure",
    "v2_nails_gal_4.jpg": "nail polish",
    "v2_hair_gal_1.jpg": "blonde hair back",
    "v2_hair_gal_3.jpg": "brunette hair waves",
    "v2_hair_gal_4.jpg": "short haircut back",
    "v2_brows_gal_3.jpg": "eyebrow plucking",
    "v2_brows_gal_4.jpg": "eyebrows makeup"
}

for filename, query in queries.items():
    print(f"Searching Wikimedia for: {query}")
    url = f"https://commons.wikimedia.org/w/api.php?action=query&format=json&generator=search&gsrnamespace=6&gsrsearch={urllib.parse.quote(query)}&gsrlimit=5&prop=imageinfo&iiprop=url"
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read())
        
        pages = data.get('query', {}).get('pages', {})
        if not pages:
            print(f"No results for {query}")
            continue
            
        # Get the first image URL
        page = list(pages.values())[0]
        img_url = page['imageinfo'][0]['url']
        print(f"Downloading {img_url}")
        
        req_img = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req_img, timeout=5) as response:
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
        print(f"Saved {filename}")
        
    except Exception as e:
        print(f"Failed {query}: {e}")
