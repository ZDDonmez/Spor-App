with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The content starts with <!DOCT<style>
# We need to extract the style content
style_start = content.find('<style>')
style_end = content.find('</style>')
style_content = content[style_start:style_end+8]

# And the body content
body_start = content.find('<body')
body_content = content[body_start:]

head_html = """<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>METRA</title>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
"""

new_content = head_html + style_content + "\n</head>\n" + body_content

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Head fixed!")
