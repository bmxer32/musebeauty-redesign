import shutil
import os

artifact_dir = r"C:\Users\buren\.gemini\antigravity\brain\e73c85df-ff43-4eae-a0db-0b29f4bf1d82"
target_dir = r"c:\autosait\assets\img"

mapping = {
    "lashes_gal_1_1785614800497.jpg": "v2_lashes_gal_1.jpg",
    "lashes_gal_2_1785614813106.jpg": "v2_lashes_gal_2.jpg",
    "brows_gal_1_1785614828751.jpg": "v2_brows_gal_1.jpg",
    "brows_gal_2_1785614842847.jpg": "v2_brows_gal_2.jpg",
    "nails_gal_1_1785614856438.jpg": "v2_nails_gal_1.jpg",
    "nails_gal_2_1785614871015.jpg": "v2_nails_gal_2.jpg",
    "luxhair_gal_1_1785614883336.jpg": "v2_luxhair_gal_1.jpg"
}

for src_name, dst_name in mapping.items():
    src_path = os.path.join(artifact_dir, src_name)
    dst_path = os.path.join(target_dir, dst_name)
    if os.path.exists(src_path):
        shutil.copy2(src_path, dst_path)
        print(f"Copied {src_name} -> {dst_name}")

print("Subpage gallery images prepared!")
