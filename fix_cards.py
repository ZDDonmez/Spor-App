import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS
css_target = """    .meal-dash-btn { 
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
    }
    .meal-dash-btn::before {
      content: ''; position: absolute; left: 0; top: 0; height: 100%; width: 4px;
      background: var(--accent-color); border-radius: 4px 0 0 4px; opacity: 0;
      transform: scaleY(0); transform-origin: bottom; transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.4s;
    }
    .meal-dash-btn::after {
      content: ''; position: absolute; left: 0; bottom: 0; height: 1px; width: 0%;
      background: var(--accent-color); transition: width 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .meal-dash-btn:hover::before { transform: scaleY(1); opacity: 1; }
    .meal-dash-btn:hover::after { width: 100%; }
    .meal-dash-btn:hover { color: var(--accent-color); transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.08); }
    .meal-dash-cal { color: var(--text-muted); font-size: 0.8rem; font-weight: 600; background: var(--surface-color); padding: 3px 6px; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.05); transition: color 0.3s; }
    .meal-dash-btn:hover .meal-dash-cal { color: var(--accent-color); }"""

css_replacement = """    .meal-dash-btn { 
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
content = content.replace(css_target, css_replacement)

# 2. Update HTML of the meal stack
html_target = """      <!-- Right: Meal Stack -->
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

html_replacement = """      <!-- Right: Meal Stack -->
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
content = content.replace(html_target, html_replacement)

# Make sure Top section layout aligns well. If buttons are very tall, ring might be centered weirdly.
# We will use align-items: stretch so they match heights or flex-start? `align-items: center` is fine.

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Meal buttons updated to visual cards!")
