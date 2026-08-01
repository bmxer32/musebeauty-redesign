import os
import sys
import json
import urllib.request

sys.stdout.reconfigure(encoding='utf-8')

IMG_DIR = os.path.join('assets', 'img')
os.makedirs(IMG_DIR, exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

with open('muse_images.json', 'r', encoding='utf-8') as f:
    img_urls = json.load(f)

print(f"Total image URLs to check: {len(img_urls)}")

downloaded = []
for idx, url in enumerate(img_urls):
    # filter out tiny icons or tracker pixels if any
    if 'favicon' in url or 'pixel' in url:
        continue
    
    ext = 'jpg'
    if '.png' in url: ext = 'png'
    elif '.webp' in url: ext = 'webp'
    elif '.svg' in url: ext = 'svg'
    
    filename = f"muse_img_{idx+1}.{ext}"
    dest_path = os.path.join(IMG_DIR, filename)
    
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read()
            if len(data) > 2000: # only keep real image files > 2KB
                with open(dest_path, 'wb') as out:
                    out.write(data)
                size = os.path.getsize(dest_path)
                downloaded.append({
                    'filename': filename,
                    'orig_url': url,
                    'size': size
                })
                print(f"Downloaded {filename}: {size} bytes ({url})")
    except Exception as e:
        pass

print(f"\nSuccessfully downloaded {len(downloaded)} valid images into assets/img/!")
with open('downloaded_images_map.json', 'w', encoding='utf-8') as f:
    json.dump(downloaded, f, ensure_ascii=False, indent=2)
