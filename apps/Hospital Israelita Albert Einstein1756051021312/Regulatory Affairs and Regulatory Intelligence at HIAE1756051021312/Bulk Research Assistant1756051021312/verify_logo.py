#!/usr/bin/env python3
import base64
import re

# Read the Python file
with open('Bulk_Research_Assistant1756051021312.py', 'r') as f:
    content = f.read()

# Extract the base64 string
pattern = r'data:image/png;base64,([A-Za-z0-9+/]*)'
match = re.search(pattern, content)

if match:
    base64_string = match.group(1)
    print(f"Base64 string length: {len(base64_string)} characters")
    
    try:
        # Decode the base64 string
        decoded_data = base64.b64decode(base64_string)
        print(f"✅ Base64 decode successful! Decoded data length: {len(decoded_data)} bytes")
        
        # Check if it starts with PNG signature
        if decoded_data[:8] == b'\x89PNG\r\n\x1a\n':
            print("✅ Valid PNG file signature detected")
        else:
            print("❌ Invalid PNG file signature")
            
    except Exception as e:
        print(f"❌ Base64 decode failed: {e}")
else:
    print("❌ No base64 string found in the file")
