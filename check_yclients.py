import sys
import re
import json
import urllib.request

sys.stdout.reconfigure(encoding='utf-8')

with open('yclients_raw.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Search for api endpoints
api_urls = re.findall(r'https://[^\s"\'\>]*/api/[^\s"\'\>]*', html)
print("API URLs:", api_urls)

# Try fetching public API services endpoint for company 549326
url = 'https://api.yclients.com/api/v1/book_services/549326'
req = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/5.0',
    'Accept': 'application/json',
    'Authorization': 'Bearer yclients' # standard or anon
})

try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        print("Success fetching YClients book_services API!")
        with open('yclients_services_full.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
except Exception as e:
    print("book_services API error:", e)
