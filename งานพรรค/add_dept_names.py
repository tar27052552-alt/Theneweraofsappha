import re

file_path = r'c:\Users\papu\งานพรรค\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to find department member cards (div with class text-center group and data-name)
# We capture the div opening tag up to the closing > of the inner div containing the image.
# Then we want to insert the <p> tag before the closing </div> of the outer div.

# The structure is:
# <div class="text-center group" ... data-name="NAME">
#     <div ...><img ...></div>
# </div>

# We will look for the pattern and replace.
# Regex Explanation:
# (<div class="text-center group"[^>]*data-name="([^"]+)"[^>]*>\s*<div[^>]*>.*?<\/div>\s*) : Capture Group 1 (Entire open div + inner div), Capture Group 2 (The Name)
# (?!<p) : Negative lookahead to make sure we haven't already added a <p> tag right after.

pattern = re.compile(
    r'(<div class="text-center group"[^>]*data-name="([^"]+)"[^>]*>\s*<div[^>]*>.*?<\/div>\s*)(?!<p)',
    re.DOTALL
)

def replacement(match):
    full_block = match.group(1)
    name = match.group(2)
    # Extract only the name part if it has nickname in parens for cleaner display?
    # User requested "Better on phone". Full name might be too long.
    # Let's keep full name but use truncation class.
    
    # Check if name is just blank or weird
    if not name or name.strip() == "":
        return full_block

    new_tag = f'<p class="text-xs font-medium text-sappha-text mt-2 truncate px-1">{name}</p>'
    return full_block + new_tag + '\n'

new_content = pattern.sub(replacement, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully injected names into department cards.")
