#!/usr/bin/env python3

# Read the complete base64 string from the file
with open('logo_base64.txt', 'r') as f:
    complete_base64 = f.read().strip()

# Read the Python file
with open('Bulk_Research_Assistant1756051021312.py', 'r') as f:
    content = f.read()

# Find the img tag and replace the entire src attribute
import re

# Pattern to match the img tag with the old base64
pattern = r'<img src="data:image/png;base64,[^"]*" alt="Barkley Logo" class="header-logo">'

# New img tag with complete base64
new_img_tag = f'<img src="data:image/png;base64,{complete_base64}" alt="Barkley Logo" class="header-logo">'

# Replace the img tag
new_content = re.sub(pattern, new_img_tag, content)

# Write back to the file
with open('Bulk_Research_Assistant1756051021312.py', 'w') as f:
    f.write(new_content)

print("Logo base64 string updated successfully!")
