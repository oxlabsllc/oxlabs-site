import re

with open("css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# 1. Darken --gold for better contrast
css = re.sub(
    r'--gold:\s*#[0-9a-fA-F]+;',
    '--gold: #5a4b33;',
    css
)

css = re.sub(
    r'--gold-light:\s*#[0-9a-fA-F]+;',
    '--gold-light: #7a6a4d;',
    css
)

# 2. Fix eyebrow: remove uppercase, change font to serif to reduce Inter usage
css = re.sub(
    r'\.eyebrow \{[^}]+\}',
    '''.eyebrow {
  font-family: var(--font-serif);
  font-size: 1rem;
  font-weight: 500;
  color: var(--gold);
  margin-bottom: 20px;
}''',
    css
)

# 3. Fix ledger th to only apply to thead, and add normal styling for tbody th
css = re.sub(
    r'\.ledger th \{[^}]+\}',
    '''.ledger thead th {
  text-align: left;
  font-family: var(--font-sans);
  font-weight: 500;
  font-style: normal;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  font-size: 0.75rem;
  color: var(--ink-soft);
  padding: 16px 24px 12px;
  border-bottom: 1px solid var(--rule);
}

.ledger tbody th {
  text-align: left;
  font-family: var(--font-sans);
  font-weight: 500;
  font-size: 0.95rem;
  color: var(--ink);
  padding: 14px 24px;
  border-bottom: 1px solid var(--rule);
  vertical-align: top;
}''',
    css
)

# 4. Fix also-fits line length
css = re.sub(
    r'\.also-fits \{([^}]+)\}',
    r'.also-fits {\1  max-width: 65ch;\n}',
    css
)

with open("css/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Fixed CSS issues")
