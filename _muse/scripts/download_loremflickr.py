import urllib.request
import os

images = {
    "v2_nails_gal_3.jpg": "https://loremflickr.com/800/600/manicure,nails",
    "v2_nails_gal_4.jpg": "https://loremflickr.com/800/600/gel,nails",
    "v2_hair_gal_1.jpg": "https://loremflickr.com/800/600/blonde,hair",
    "v2_hair_gal_3.jpg": "https://loremflickr.com/800/600/wavy,hair,salon",
    "v2_hair_gal_4.jpg": "https://loremflickr.com/800/600/haircut,woman",
    "v2_brows_gal_3.jpg": "https://loremflickr.com/800/600/eyebrows,plucking",
    "v2_brows_gal_4.jpg": "https://loremflickr.com/800/600/eyebrow,makeup"
}

for filename, url in images.items():
    print(f"Downloading {filename}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            with open(os.path.join("assets/img", filename), "wb") as f:
                f.write(response.read())
        print(f"Success: {filename}")
    except Exception as e:
        print(f"Error downloading {filename}: {e}")
