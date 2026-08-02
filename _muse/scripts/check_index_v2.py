with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'src="[^"]+"', text)
for m in matches:
    if 'v2_' in m:
        print("Found:", m)
