import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS for meal-dash-btn (remove overflow: hidden) and add .meal-tooltip
css_target = """    .meal-dash-btn { 
      background: var(--bg-color); border: 1px solid var(--surface-border);
      border-radius: 14px; padding: 8px 12px; color: var(--text-color); font-family: var(--font-body); font-weight: 600; font-size: 0.85rem;
      cursor: pointer; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); display: flex; justify-content: space-between; align-items: center;
      box-shadow: 0 2px 8px rgba(0,0,0,0.03); position: relative; overflow: hidden; margin-bottom: 2px;
    }"""
css_replacement = """    .meal-dash-btn { 
      background: var(--bg-color); border: 1px solid var(--surface-border);
      border-radius: 14px; padding: 8px 12px; color: var(--text-color); font-family: var(--font-body); font-weight: 600; font-size: 0.85rem;
      cursor: pointer; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); display: flex; justify-content: space-between; align-items: center;
      box-shadow: 0 2px 8px rgba(0,0,0,0.03); position: relative; margin-bottom: 2px;
    }
    
    .meal-tooltip {
      position: absolute;
      top: 50%;
      right: calc(100% + 4px); /* Starts slightly closer */
      transform: translateY(-50%) scale(0.9);
      width: 140px;
      height: 90px;
      background-size: cover;
      background-position: center;
      border-radius: 12px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.2);
      opacity: 0;
      visibility: hidden;
      transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
      z-index: 100;
      pointer-events: none;
      border: 2px solid var(--surface-color);
    }
    
    .meal-dash-btn:hover .meal-tooltip {
      opacity: 1;
      visibility: visible;
      transform: translateY(-50%) scale(1);
      right: calc(100% + 12px); /* Glides outwards to the left */
    }"""
content = content.replace(css_target, css_replacement)

# 2. Add tooltips to HTML buttons
html_target = """      <!-- Right: Meal Stack -->
      <div style="flex: 1.2; display: flex; flex-direction: column;">
        <button class="meal-dash-btn" data-category="breakfast">
          Kahvaltı <span id="cal-breakfast" class="meal-dash-cal">0</span>
        </button>
        <button class="meal-dash-btn" data-category="lunch">
          Öğle <span id="cal-lunch" class="meal-dash-cal">0</span>
        </button>
        <button class="meal-dash-btn" data-category="dinner">
          Akşam <span id="cal-dinner" class="meal-dash-cal">0</span>
        </button>
        <button class="meal-dash-btn" data-category="snack">
          Ara Öğün <span id="cal-snack" class="meal-dash-cal">0</span>
        </button>
      </div>"""
html_replacement = """      <!-- Right: Meal Stack -->
      <div style="flex: 1.2; display: flex; flex-direction: column;">
        <button class="meal-dash-btn" data-category="breakfast">
          Kahvaltı <span id="cal-breakfast" class="meal-dash-cal">0</span>
          <div class="meal-tooltip" style="background-image: url('breakfast_bg.png');"></div>
        </button>
        <button class="meal-dash-btn" data-category="lunch">
          Öğle <span id="cal-lunch" class="meal-dash-cal">0</span>
          <div class="meal-tooltip" style="background-image: url('lunch_bg.png');"></div>
        </button>
        <button class="meal-dash-btn" data-category="dinner">
          Akşam <span id="cal-dinner" class="meal-dash-cal">0</span>
          <div class="meal-tooltip" style="background-image: url('dinner_bg.png');"></div>
        </button>
        <button class="meal-dash-btn" data-category="snack">
          Ara Öğün <span id="cal-snack" class="meal-dash-cal">0</span>
          <div class="meal-tooltip" style="background-image: url('snack_bg.png');"></div>
        </button>
      </div>"""
content = content.replace(html_target, html_replacement)


# 3. Force default white theme
# Replace localStorage logic if necessary, or just override
js_target = "const savedTheme = localStorage.getItem('antigravity_theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');"
js_target2 = "const savedTheme = localStorage.getItem('antigravity_theme') || 'light';"

js_replacement = "const savedTheme = localStorage.getItem('antigravity_theme') || 'light';"

if js_target in content:
    content = content.replace(js_target, js_replacement)
elif "localStorage.getItem('antigravity_theme')" in content:
    # Use regex to force it to light
    content = re.sub(r"const savedTheme = localStorage\.getItem\('antigravity_theme'\).*?;", js_replacement, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Tooltips and default white theme added!")
