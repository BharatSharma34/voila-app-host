#!/usr/bin/env python3
import base64
import re

# Read the logo file and encode it properly
with open('barkleyGPT copy.png', 'rb') as f:
    logo_data = f.read()

# Encode to base64
logo_base64 = base64.b64encode(logo_data).decode('utf-8')

# Read the Python file
with open('Bulk_Research_Assistant1756051021312.py', 'r') as f:
    content = f.read()

# Create the new img tag with the proper base64 string
new_img_tag = f'<img src="data:image/png;base64,{logo_base64}" alt="Barkley Logo" class="header-logo">'

# Find and replace the img tag
pattern = r'<img src="data:image/png;base64,[^"]*" alt="Barkley Logo" class="header-logo">'
new_content = re.sub(pattern, new_img_tag, content)

# Write back to the file
with open('Bulk_Research_Assistant1756051021312.py', 'w') as f:
    f.write(new_content)

print("Logo updated successfully!")
print(f"Base64 string length: {len(logo_base64)} characters")
