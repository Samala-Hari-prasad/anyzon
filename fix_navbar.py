import re

path = 'templates/anyzone/base.html'
content = open(path, encoding='utf-8').read()

# Patch: replace the href="#" Account link with the profile URL
old = 'href="#" class="nav-link-az me-2"'
new = 'href="{% url \'user_profile\' %}" class="nav-link-az me-2" id="nav-account"'

# Also patch "Hello, sign in" → "Hello, Aarav"
if old in content:
    content = content.replace(old, new, 1)
    content = content.replace('Hello, sign in', 'Hello, Aarav', 1)
    open(path, 'w', encoding='utf-8').write(content)
    print("✅ base.html patched successfully.")
else:
    print("⚠️  Pattern not found – check manually.")
