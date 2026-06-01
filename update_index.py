import re

with open('src/pages/index.astro', 'r') as f:
    content = f.read()

with open('states_out.txt', 'r') as f:
    states_out = f.read()

html_options = states_out.split('=== HTML OPTIONS ===\n')[1].split('=== JSON DATA ===\n')[0].strip()
json_data = states_out.split('=== JSON DATA ===\n')[1].strip()

# Replace HTML select options
html_pattern = re.compile(r'(<select id="state" class="input-field font-medium bg-white">).*?(</select>)', re.DOTALL)
content = html_pattern.sub(r'\1\n' + html_options + r'\n\t\t\t\t\t\t\t\2', content)

# Replace JS object
js_pattern = re.compile(r'(const stateTaxData: Record<string, any> = )\{.*?\};', re.DOTALL)
content = js_pattern.sub(r'\1' + json_data + ';', content)

with open('src/pages/index.astro', 'w') as f:
    f.write(content)

print("Updated index.astro")
