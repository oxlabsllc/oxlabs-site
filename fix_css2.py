import re

with open("css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# 1. Make --gold-light much lighter for contrast against dark navy
css = re.sub(
    r'--gold-light:\s*#[0-9a-fA-F]+;',
    '--gold-light: #e0d0b5;',
    css
)

# 2. Reduce Inter font usage by making the ledger body row headers serif (inherit from body)
css = re.sub(
    r'(\.ledger tbody th \{[^}]*)font-family:\s*var\(--font-sans\);\s*',
    r'\1',
    css
)

with open("css/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Fixed CSS issues")
