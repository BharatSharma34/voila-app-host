#!/usr/bin/env python3
import base64

# Read the base64 string from the file
with open('final_test_base64.txt', 'r') as f:
    base64_string = f.read().strip()

try:
    # Decode the base64 string
    decoded_data = base64.b64decode(base64_string)
    
    # Write to a file
    with open('test_decoded.png', 'wb') as f:
        f.write(decoded_data)
    
    print("Base64 decode successful!")
    print(f"Decoded data length: {len(decoded_data)} bytes")
    
except Exception as e:
    print(f"Base64 decode failed: {e}")
