import os
import shutil

img_dir = "assets/img"

rename_map = {
    "lashes_category.jpg": "v2_lashes.jpg",
    "brows_category.jpg": "v2_brows.jpg",
    "nails_category.jpg": "v2_nails.jpg",
    "luxhair_category.jpg": "v2_luxhair.jpg",
    "hair_category.jpg": "v2_hair.jpg",
    "makeup_category.jpg": "v2_makeup.jpg"
}

for old_name, new_name in rename_map.items():
    old_path = os.path.join(img_dir, old_name)
    new_path = os.path.join(img_dir, new_name)
    if os.path.exists(old_path):
        shutil.copy2(old_path, new_path)
        print(f"Renamed/copied {old_name} -> {new_name}")

print("V2 cache-busting image filenames created!")
