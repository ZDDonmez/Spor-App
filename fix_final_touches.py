with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove 🌍 from Egzersiz
content = content.replace('<h2 class="section-title" style="margin: 0; font-size: 1.1rem; gap: 6px;">🌍 Egzersiz</h2>', '<h2 class="section-title" style="margin: 0; font-size: 1.1rem; gap: 6px;">Egzersiz</h2>')


# 2. Add Burned Calories under the ring
ring_parent_target = """        <p id="goal-exceeded-msg" class="info-text" style="color: var(--error-color); text-align: center; display: none; margin-top: 12px; font-size: 0.85rem;">Hedef aşıldı!</p>
      </div>"""
ring_parent_replacement = """        <div style="font-size: 0.85rem; color: #f59e0b; font-weight: 600; margin-top: 8px;">🔥 <span id="ring-burned-cal-display">0</span> kcal yakıldı</div>
        <p id="goal-exceeded-msg" class="info-text" style="color: var(--error-color); text-align: center; display: none; margin-top: 8px; font-size: 0.85rem;">Hedef aşıldı!</p>
      </div>"""
content = content.replace(ring_parent_target, ring_parent_replacement)

# JS update for ring-burned-cal-display
ui_update_target = """      el.liveCal.textContent = currentWalkCal;
    }"""
ui_update_replacement = """      el.liveCal.textContent = currentWalkCal;
    }
    
    const burnedDisplay = document.getElementById('ring-burned-cal-display');
    if (burnedDisplay) burnedDisplay.textContent = state.burnedCalories;"""
content = content.replace(ui_update_target, ui_update_replacement)


# 3. Add gliding border effect to the meal tabs
meal_css_target = """    .meal-dash-btn::before {
      content: ''; position: absolute; left: 0; top: 0; height: 100%; width: 4px;
      background: var(--accent-color); border-radius: 4px 0 0 4px; opacity: 0.8;
    }
    .meal-dash-btn:hover { border-color: var(--accent-color); color: var(--accent-color); transform: translateY(-2px); box-shadow: 0 4px 10px rgba(0,0,0,0.06); }"""

meal_css_replacement = """    .meal-dash-btn::before {
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
    .meal-dash-btn:hover { color: var(--accent-color); transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.08); }"""
content = content.replace(meal_css_target, meal_css_replacement)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Final touches applied!")
