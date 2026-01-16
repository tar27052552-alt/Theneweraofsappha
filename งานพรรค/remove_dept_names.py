import re

file_path = r'c:\Users\papu\งานพรรค\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to find the specific p tag we added
# <p class="text-xs font-medium text-sappha-text mt-2 truncate px-1">...</p>
pattern = re.compile(
    r'\s*<p class="text-xs font-medium text-sappha-text mt-2 truncate px-1">.*?</p>',
    re.DOTALL
)

new_content = pattern.sub('', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully removed injected names from department cards.")
