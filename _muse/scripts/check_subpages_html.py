import os

for fname in ['lashes.html', 'brows.html', 'nails.html', 'luxhair.html', 'hair.html', 'makeup.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    print(f"{fname}: len={len(content)}, has_gallery={'gallery-grid' in content}")
