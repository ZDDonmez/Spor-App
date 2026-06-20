with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("function initMapPlaceholder() {", "let map, marker, pathLine;\n    function initMapPlaceholder() {")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Variables restored")
