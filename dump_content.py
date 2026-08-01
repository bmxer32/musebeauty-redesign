import sys
import json
import re
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

with open('raw_muse.html', 'rb') as f:
    html = f.read().decode('utf-8', errors='ignore')

soup = BeautifulSoup(html, 'html.parser')

# Clean text dump
lines = []
for el in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'div', 'span', 'li', 'td', 'a']):
    t = el.get_text(strip=True)
    if t and len(el.find_all()) == 0 and len(t) > 1:
        if not lines or lines[-1] != t:
            lines.append(t)

with open('muse_texts.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

# Image URLs
urls = set()
for match in re.finditer(r'https?://[^\s"\'\)\>]+\.(?:jpg|jpeg|png|webp|svg|gif)', html, re.IGNORECASE):
    u = match.group(0)
    if 'tilda' in u or 'static' in u or 'muse' in u or 'uploads' in u:
        urls.add(u)

with open('muse_images.json', 'w', encoding='utf-8') as f:
    json.dump(list(urls), f, ensure_ascii=False, indent=2)

print(f"Dumped {len(lines)} text blocks to muse_texts.txt")
print(f"Dumped {len(urls)} image URLs to muse_images.json")
