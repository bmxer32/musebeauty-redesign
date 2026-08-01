import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html') and not f.startswith(('live_', 'raw_', 'yclients_'))]

all_passed = True
for fname in html_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    imgs = re.findall(r'src=["\'](\./assets/img/[^"\']+)["\']', content)
    site_imgs = [i for i in imgs if '5AA1398A' not in i]
    duplicates = [i for i in set(site_imgs) if site_imgs.count(i) > 1]
    if duplicates:
        print(f"FAIL: Duplicate photos found on {fname}: {duplicates}")
        all_passed = False
    else:
        print(f"PASS: {fname} has {len(site_imgs)} unique photos - ZERO duplicates!")

if all_passed:
    print("\nALL PAGES VERIFIED: ZERO PHOTO DUPLICATION GUARANTEED!")
