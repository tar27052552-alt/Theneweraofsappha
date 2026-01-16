import re
import os

file_path = "index.html"
# Ensure absolute path or rely on CWD
# We will use relative path assuming running from CWD

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Pattern to find the department member blocks
pattern = r'(<div class="text-center group" data-room="(.*?)">)(\s*<div.*?<\/div>)(\s*<p[^>]*>)([\s\S]*?)(<\/p>)'

def replacement(match):
    div_start = match.group(1)
    room = match.group(2)
    img_div = match.group(3)
    p_start = match.group(4)
    name_raw = match.group(5)
    p_end = match.group(6)
    
    # Clean the name (remove newlines and extra spaces)
    name_clean = re.sub(r'\s+', ' ', name_raw).strip()
    
    # Reconstruct
    new_div_start = f'<div class="text-center group" data-room="{room}" data-name="{name_clean}">'
    
    return f'{new_div_start}{img_div}'

new_content, count = re.subn(pattern, replacement, content)

print(f"Found {count} matches to replace.")

if count > 0:
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("File updated successfully.")
else:
    print("No matches found.")
