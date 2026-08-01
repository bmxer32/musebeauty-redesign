import sys
import json
import re
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

with open('raw_muse.html', 'rb') as f:
    html = f.read().decode('utf-8', errors='ignore')

soup = BeautifulSoup(html, 'html.parser')

title = soup.title.string.strip() if soup.title else ''
meta_desc = ''
meta_tag = soup.find('meta', {'name': 'description'})
if meta_tag and meta_tag.get('content'):
    meta_desc = meta_tag['content'].strip()

out = {
    'title': title,
    'meta_description': meta_desc,
    'sections': [],
    'all_texts': [],
    'images': [],
    'links': [],
    'iframes': []
}

# Collect all images
for img in soup.find_all('img'):
    src = img.get('src') or img.get('data-original') or img.get('data-tu-src')
    alt = img.get('alt', '')
    if src:
        out['images'].append({'src': src, 'alt': alt})

# Collect all links
for a in soup.find_all('a', href=True):
    out['links'].append({'href': a['href'], 'text': a.get_text(strip=True)})

# Collect all iframes (maps, widgets)
for iframe in soup.find_all('iframe'):
    out['iframes'].append({'src': iframe.get('src')})

# Collect Tilda record blocks
records = soup.find_all('div', class_=re.compile(r'r_') or re.compile(r't-rec'))
for rec in records:
    rec_id = rec.get('id', '')
    # text inside
    texts = [p.get_text(strip=True) for p in rec.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li', 'div', 'span']) if p.get_text(strip=True) and len(p.find_all()) == 0]
    if texts:
        out['sections'].append({
            'rec_id': rec_id,
            'texts': texts[:20]
        })

with open('parsed_muse.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print('Parsing complete!')
print('Images count:', len(out['images']))
print('Links count:', len(out['links']))
print('Sections count:', len(out['sections']))
