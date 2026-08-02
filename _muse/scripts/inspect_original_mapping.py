import json

with open('parsed_blocks.json', 'r', encoding='utf-8') as f:
    blocks = json.load(f)

for i, b in enumerate(blocks):
    print(f"\n==================== BLOCK {i} ({b['block_id']}) ====================")
    print("Headings:", b['headings'])
    print("Texts snippet:", [t[:100] for t in b['texts'][:3]])
    print("Images:")
    for img in b['images']:
        print("  -", img)
