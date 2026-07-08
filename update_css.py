import re

with open("css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# 1. Root variables
css = re.sub(
    r':root \{.*?\n\}',
    ''':root {
  --cream: #ffffff;
  --cream-deep: #f8f9fa;
  --navy: #0b132b;
  --navy-deep: #050a17;
  --ink: #1c202a;
  --ink-soft: #5b6270;
  --gold: #8e7d5b;
  --gold-light: #ab9d80;
  --rule: rgba(11, 19, 43, 0.12);
  --rule-strong: rgba(11, 19, 43, 0.25);
  --rule-light: rgba(255, 255, 255, 0.2);
  --cream-muted: rgba(255, 255, 255, 0.7);
  --font-serif: "EB Garamond", Garamond, Georgia, "Times New Roman", serif;
  --font-sans: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  --header-h: 80px;
}''',
    css,
    flags=re.DOTALL
)

# 2. Body
css = re.sub(
    r'body \{[^}]+\}',
    '''body {
  font-family: var(--font-serif);
  font-size: 1.125rem;
  line-height: 1.6;
  color: var(--ink);
  background-color: var(--cream);
  -webkit-font-smoothing: antialiased;
}''',
    css,
    count=1
)

# 3. Eyebrow
css = re.sub(
    r'\.eyebrow \{[^}]+\}',
    '''.eyebrow {
  font-family: var(--font-sans);
  font-size: 0.8rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--gold);
  margin-bottom: 20px;
}''',
    css,
    count=1
)

# 4. Brand
css = re.sub(
    r'\.brand \{[^}]+\}',
    '''.brand {
  font-family: var(--font-sans);
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--navy);
}''',
    css,
    count=1
)

# 5. Nav link
css = re.sub(
    r'\.nav-link \{[^}]+\}',
    '''.nav-link {
  font-family: var(--font-sans);
  font-size: 0.9rem;
  font-weight: 500;
  color: var(--navy);
  transition: opacity 0.2s;
}''',
    css,
    count=1
)

# 6. Button
css = re.sub(
    r'\.btn \{[^}]+\}',
    '''.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 14px 32px;
  border: 1px solid var(--navy);
  border-radius: 4px;
  font-family: var(--font-sans);
  font-size: 0.85rem;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  line-height: 1.2;
  cursor: pointer;
  background: var(--navy);
  color: var(--cream);
  transition: all 0.25s ease;
}''',
    css,
    count=1
)

# Button hover
css = re.sub(
    r'\.btn:hover \{[^}]+\}',
    '''.btn:hover {
  background: var(--navy-deep);
  border-color: var(--navy-deep);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(11, 19, 43, 0.15);
}''',
    css,
    count=1
)

# Button small
css = re.sub(
    r'\.btn-small \{[^}]+\}',
    '''.btn-small {
  padding: 10px 20px;
  font-size: 0.8rem;
}''',
    css,
    count=1
)

# 7. Section bordered
css = re.sub(
    r'\.section-bordered \{[^}]+\}',
    '''.section-bordered {
  border-top: 1px solid var(--rule);
}''',
    css,
    count=1
)

# 8. Ledger
css = re.sub(
    r'\.ledger \{[^}]+\}',
    '''.ledger {
  border: 1px solid var(--rule-strong);
  background: var(--cream-deep);
  border-radius: 6px;
  box-shadow: 0 8px 30px rgba(11, 19, 43, 0.04);
  overflow: hidden;
}''',
    css,
    count=1
)

# Ledger head
css = re.sub(
    r'\.ledger-head \{[^}]+\}',
    '''.ledger-head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 16px;
  padding: 20px 24px;
  border-bottom: 1px solid var(--rule);
  background: #ffffff;
  font-family: var(--font-sans);
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--navy);
}''',
    css,
    count=1
)

# Ledger table th
css = re.sub(
    r'\.ledger th \{[^}]+\}',
    '''.ledger th {
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
}''',
    css,
    count=1
)

# Text link
css = re.sub(
    r'\.text-link \{[^}]+\}',
    '''.text-link {
  font-family: var(--font-sans);
  font-size: 0.95rem;
  font-weight: 500;
  color: var(--gold);
  text-decoration: underline;
  text-underline-offset: 4px;
  transition: opacity 0.3s;
}''',
    css,
    count=1
)

# Headers (h1, h2, h3)
css = re.sub(
    r'h1,\s*h2,\s*h3\s*\{[^}]+\}',
    '''h1,\nh2,\nh3 {
  font-weight: 500;
  line-height: 1.15;
  color: var(--navy);
  text-wrap: balance;
  letter-spacing: -0.015em;
}''',
    css,
    count=1
)

# Add reveal classes to the end
if ".reveal {" not in css:
    css += '''

/* ---------- Animations ---------- */
.reveal {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.8s ease-out, transform 0.8s ease-out;
}

.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}
'''

with open("css/style.css", "w", encoding="utf-8") as f:
    f.write(css)
print("Updated style.css")
