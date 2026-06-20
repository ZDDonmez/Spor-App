import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

js_match = re.search(r'<script>(.*?)</script>', content, re.DOTALL)
if js_match:
    js_code = js_match.group(1)
    with open('test.js', 'w', encoding='utf-8') as jsf:
        jsf.write(js_code)
    import subprocess
    try:
        # Check syntax using python's basic js parser or just run node if possible? Node wasn't found.
        # We can't run the JS.
        print("JS extracted to test.js")
    except Exception as e:
        print(e)
else:
    print("No JS found")
