import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS
css_target = """    .meal-dash-btn { 
      background-color: var(--surface-color);
      background-size: cover;
      background-position: center;
      border: 1px solid var(--surface-border);
      border-radius: 16px; padding: 16px 20px; color: #fff; font-family: var(--font-body); font-weight: 700; font-size: 1rem;
      cursor: pointer; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); display: flex; justify-content: space-between; align-items: center;
      box-shadow: 0 4px 12px rgba(0,0,0,0.08); position: relative; margin-bottom: 8px; overflow: hidden;
      text-shadow: 0 2px 4px rgba(0,0,0,0.8);
      letter-spacing: 0.5px;
    }
    
    .meal-dash-btn:hover { transform: translateY(-3px) scale(1.02); box-shadow: 0 8px 24px rgba(0,0,0,0.15); border-color: var(--accent-color); }
    .meal-dash-cal { color: #111; font-size: 0.85rem; font-weight: 700; background: #fff; padding: 4px 10px; border-radius: 12px; box-shadow: 0 2px 6px rgba(0,0,0,0.2); transition: transform 0.3s; text-shadow: none; }
    .meal-dash-btn:hover .meal-dash-cal { transform: scale(1.05); }"""

css_replacement = """    .meal-dash-btn { 
      background-color: var(--bg-color);
      border: 1px solid var(--surface-border);
      border-radius: 16px; padding: 12px 16px; color: var(--text-color); font-family: var(--font-body); font-weight: 600; font-size: 0.95rem;
      cursor: pointer; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); display: flex; justify-content: space-between; align-items: center;
      box-shadow: 0 2px 8px rgba(0,0,0,0.03); position: relative; margin-bottom: 8px; overflow: hidden;
      min-height: 48px;
    }
    
    .meal-dash-btn span { position: relative; z-index: 2; transition: color 0.4s; }
    
    .meal-dash-btn::before {
      content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
      background-size: cover; background-position: center;
      opacity: 0; transition: opacity 0.4s cubic-bezier(0.4, 0, 0.2, 1), transform 0.5s ease-out;
      transform: scale(1.1); z-index: 0;
    }
    .meal-dash-btn::after {
      content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
      background: linear-gradient(to right, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0.1) 100%);
      opacity: 0; transition: opacity 0.4s ease; z-index: 1;
    }
    
    .meal-dash-btn[data-category="breakfast"]::before { background-image: url('breakfast_bg.png'); }
    .meal-dash-btn[data-category="lunch"]::before { background-image: url('lunch_bg.png'); }
    .meal-dash-btn[data-category="dinner"]::before { background-image: url('dinner_bg.png'); }
    .meal-dash-btn[data-category="snack"]::before { background-image: url('snack_bg.png'); }
    
    .meal-dash-btn:hover { 
      padding: 32px 20px; color: #ffffff; 
      border-color: var(--accent-color); box-shadow: 0 8px 24px rgba(0,0,0,0.15);
      text-shadow: 0 2px 4px rgba(0,0,0,0.8);
    }
    .meal-dash-btn:hover span { color: #ffffff; }
    .meal-dash-btn:hover::before { opacity: 1; transform: scale(1); }
    .meal-dash-btn:hover::after { opacity: 1; }
    
    .meal-dash-cal { color: var(--text-muted); font-size: 0.85rem; font-weight: 600; background: var(--surface-color); padding: 4px 10px; border-radius: 12px; box-shadow: 0 2px 6px rgba(0,0,0,0.05); transition: all 0.4s; }
    .meal-dash-btn:hover .meal-dash-cal { color: #111; background: #ffffff; text-shadow: none; box-shadow: 0 4px 12px rgba(0,0,0,0.3); transform: scale(1.05); }"""
content = content.replace(css_target, css_replacement)

# 2. Update HTML
html_target = """      <!-- Right: Meal Stack -->
      <div style="flex: 1.2; display: flex; flex-direction: column;">
        <button class="meal-dash-btn" data-category="breakfast" style="background-image: linear-gradient(to right, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0.1) 100%), url('breakfast_bg.png');">
          Kahvaltı <span id="cal-breakfast" class="meal-dash-cal">0</span>
        </button>
        <button class="meal-dash-btn" data-category="lunch" style="background-image: linear-gradient(to right, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0.1) 100%), url('lunch_bg.png');">
          Öğle <span id="cal-lunch" class="meal-dash-cal">0</span>
        </button>
        <button class="meal-dash-btn" data-category="dinner" style="background-image: linear-gradient(to right, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0.1) 100%), url('dinner_bg.png');">
          Akşam <span id="cal-dinner" class="meal-dash-cal">0</span>
        </button>
        <button class="meal-dash-btn" data-category="snack" style="background-image: linear-gradient(to right, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0.1) 100%), url('snack_bg.png');">
          Ara Öğün <span id="cal-snack" class="meal-dash-cal">0</span>
        </button>
      </div>"""

html_replacement = """      <!-- Right: Meal Stack -->
      <div style="flex: 1.2; display: flex; flex-direction: column;">
        <button class="meal-dash-btn" data-category="breakfast">
          <span>Kahvaltı</span> <span id="cal-breakfast" class="meal-dash-cal">0</span>
        </button>
        <button class="meal-dash-btn" data-category="lunch">
          <span>Öğle</span> <span id="cal-lunch" class="meal-dash-cal">0</span>
        </button>
        <button class="meal-dash-btn" data-category="dinner">
          <span>Akşam</span> <span id="cal-dinner" class="meal-dash-cal">0</span>
        </button>
        <button class="meal-dash-btn" data-category="snack">
          <span>Diğer :)</span> <span id="cal-snack" class="meal-dash-cal">0</span>
        </button>
      </div>"""
content = content.replace(html_target, html_replacement)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Interactive hover reveal cards implemented!")
