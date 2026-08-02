import shutil
import os

artifact_dir = r"C:\Users\buren\.gemini\antigravity\brain\e73c85df-ff43-4eae-a0db-0b29f4bf1d82"
target_dir = r"c:\autosait\assets\img"

mapping = {
    "lashes_service_1785614259178.jpg": "lashes_category.jpg",
    "brows_service_1785614278670.jpg": "brows_category.jpg",
    "nails_service_1785614292053.jpg": "nails_category.jpg",
    "luxhair_service_1785614306211.jpg": "luxhair_category.jpg",
    "hair_salon_service_1785614322495.jpg": "hair_category.jpg",
    "makeup_service_1785614338998.jpg": "makeup_category.jpg"
}

for src_name, dst_name in mapping.items():
    src_path = os.path.join(artifact_dir, src_name)
    dst_path = os.path.join(target_dir, dst_name)
    if os.path.exists(src_path):
        shutil.copy2(src_path, dst_path)
        print(f"Copied {src_name} -> {dst_name} ({os.path.getsize(dst_path)} bytes)")
    else:
        print(f"ERROR: {src_path} not found!")

print("All generated category images copied successfully!")
