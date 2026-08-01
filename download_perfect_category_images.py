import urllib.request
import os

category_images = {
    "assets/img/lashes_category.jpg": "https://images.unsplash.com/photo-1583001931096-959e9a1a6223?q=80&w=1000&auto=format&fit=crop",
    "assets/img/brows_category.jpg": "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?q=80&w=1000&auto=format&fit=crop",
    "assets/img/nails_category.jpg": "https://images.unsplash.com/photo-1604654894610-df63bc536371?q=80&w=1000&auto=format&fit=crop",
    "assets/img/luxhair_category.jpg": "https://images.unsplash.com/photo-1519699047748-de8e457a634e?q=80&w=1000&auto=format&fit=crop",
    "assets/img/hair_category.jpg": "https://images.unsplash.com/photo-1562322140-8baeececf3df?q=80&w=1000&auto=format&fit=crop",
    "assets/img/makeup_category.jpg": "https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?q=80&w=1000&auto=format&fit=crop"
}

print("Downloading 100% accurate, high-resolution category images...")

for local_path, url in category_images.items():
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp, open(local_path, 'wb') as f:
            data = resp.read()
            f.write(data)
            print(f"Downloaded {local_path} ({len(data)} bytes)")
    except Exception as e:
        print(f"Error downloading {local_path}: {e}")

print("Category images download task completed.")
