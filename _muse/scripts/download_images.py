from duckduckgo_search import DDGS
from urllib.request import Request, urlopen
from PIL import Image
from io import BytesIO
import os
import time

queries = {
    "v2_nails_gal_3.jpg": "close up professional hardware manicure salon",
    "v2_nails_gal_4.jpg": "perfect gel polish manicure nude pastel close up",
    "v2_hair_gal_1.jpg": "beautiful blonde airtouch balayage hair back view salon",
    "v2_hair_gal_3.jpg": "brown hair waves back view salon",
    "v2_hair_gal_4.jpg": "stylish bob haircut female back view",
    "v2_brows_gal_3.jpg": "plucking eyebrows tweezers close up beauty salon",
    "v2_brows_gal_4.jpg": "thick laminated eyebrows close up natural"
}

ddgs = DDGS()

for filename, query in queries.items():
    print(f"Searching for {filename}: {query}")
    results = ddgs.images(query, max_results=3, size="Large")
    if not results:
        print(f"No results for {query}")
        continue
    
    for res in results:
        url = res["image"]
        try:
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urlopen(req, timeout=5) as response:
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
            print(f"Saved {filename} from {url}")
            break
        except Exception as e:
            print(f"Failed {url}: {e}")
    time.sleep(1)
