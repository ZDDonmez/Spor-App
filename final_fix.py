import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix Meal Dash Buttons CSS
meal_btn_target = """    .meal-dash-btn { 
      background: var(--bg-color); border: 1px solid var(--surface-border);
      border-radius: 12px; padding: 12px 16px; color: var(--text-color); font-family: var(--font-body); font-weight: 600; font-size: 0.95rem;
      cursor: pointer; transition: all 0.2s ease; display: flex; justify-content: space-between; align-items: center;
      box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    .meal-dash-btn:hover { border-color: var(--accent-color); color: var(--accent-color); transform: translateY(-1px); box-shadow: 0 4px 8px rgba(0,0,0,0.05); }
    .meal-dash-cal { color: var(--text-muted); font-size: 0.9rem; font-weight: 400; transition: color 0.3s; }
    .meal-dash-btn:hover .meal-dash-cal { color: var(--accent-color); }"""

meal_btn_replacement = """    .meal-dash-btn { 
      background: var(--bg-color); border: 1px solid var(--surface-border);
      border-radius: 16px; padding: 10px 14px; color: var(--text-color); font-family: var(--font-body); font-weight: 600; font-size: 0.9rem;
      cursor: pointer; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); display: flex; justify-content: space-between; align-items: center;
      box-shadow: 0 2px 8px rgba(0,0,0,0.03); position: relative; overflow: hidden;
    }
    .meal-dash-btn::before {
      content: ''; position: absolute; left: 0; top: 0; height: 100%; width: 4px;
      background: var(--accent-color); border-radius: 4px 0 0 4px; opacity: 0.8;
    }
    .meal-dash-btn:hover { border-color: var(--accent-color); color: var(--accent-color); transform: translateY(-2px); box-shadow: 0 6px 12px rgba(0,0,0,0.08); }
    .meal-dash-cal { color: var(--text-muted); font-size: 0.85rem; font-weight: 600; background: var(--surface-color); padding: 4px 8px; border-radius: 10px; box-shadow: 0 1px 3px rgba(0,0,0,0.05); transition: color 0.3s; }
    .meal-dash-btn:hover .meal-dash-cal { color: var(--accent-color); }"""
content = content.replace(meal_btn_target, meal_btn_replacement)


# 2. Fix the Ring Container and HTML
ring_html_target = """        <div class="ring-container" style="position: relative; margin: 0; width: 100%; max-width: 140px; aspect-ratio: 1/1; display: flex; justify-content: center; align-items: center;">
          <svg class="ring-svg" viewBox="0 0 220 220" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; transform: rotate(-90deg);">
            <circle class="ring-bg" cx="110" cy="110" r="104"></circle>
            <circle class="ring-burned" id="calorie-ring-burned" cx="110" cy="110" r="104"></circle>
            <circle class="ring-progress" id="calorie-ring" cx="110" cy="110" r="104"></circle>
          </svg>
          <div class="calories-info" style="position: relative; z-index: 2; display: flex; flex-direction: column; align-items: center; justify-content: center; margin-top: 0;">
            <div class="main-cal" style="font-family: var(--font-heading); font-size: 2rem; font-weight: 700; color: var(--text-color); line-height: 1;">
              <span id="calories-consumed-main">0</span>
            </div>
            <div style="font-size: 0.8rem; color: var(--text-muted); margin-top: 2px; font-weight: 500;">kcal</div>
            <div style="font-size: 0.7rem; color: var(--text-muted); opacity: 0.8; margin-top: 4px;">Hedef: <span id="calories-goal">2000</span></div>
          </div>
        </div>"""

ring_html_replacement = """        <div class="ring-container" style="position: relative; margin: 0; width: 100%; max-width: 150px; aspect-ratio: 1/1; display: block;">
          <svg class="ring-svg" viewBox="0 0 220 220" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; transform: rotate(-90deg);">
            <circle class="ring-bg" cx="110" cy="110" r="96"></circle>
            <circle class="ring-burned" id="calorie-ring-burned" cx="110" cy="110" r="96"></circle>
            <circle class="ring-progress" id="calorie-ring" cx="110" cy="110" r="96"></circle>
          </svg>
          <div class="calories-info" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 2; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <div class="main-cal" style="font-family: var(--font-heading); font-size: 1.8rem; font-weight: 700; color: var(--text-color); line-height: 1;">
              <span id="calories-consumed-main">0</span>
            </div>
            <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 2px; font-weight: 600;">kcal</div>
            <div style="font-size: 0.7rem; color: var(--text-muted); opacity: 0.8; margin-top: 4px;">Hedef: <span id="calories-goal">2000</span></div>
          </div>
        </div>"""
content = content.replace(ring_html_target, ring_html_replacement)

# Update RING_CIRCUMFERENCE in JS
content = content.replace("const RING_CIRCUMFERENCE = 2 * Math.PI * 104;", "const RING_CIRCUMFERENCE = 2 * Math.PI * 96;")

# Gliding effect for ring CSS
ring_css_target = """    .ring-progress { fill: none; stroke: var(--accent-color); stroke-width: 16; stroke-linecap: round; transition: stroke-dashoffset 1s cubic-bezier(0.4, 0, 0.2, 1); filter: drop-shadow(0 0 6px var(--accent-glow)); }
    .ring-burned { fill: none; stroke: #FF9800; /* Orange for burned */ stroke-width: 16; stroke-linecap: round; transition: stroke-dashoffset 1s cubic-bezier(0.4, 0, 0.2, 1); filter: drop-shadow(0 0 6px rgba(255, 152, 0, 0.4)); }"""
ring_css_replacement = """    .ring-progress { fill: none; stroke: var(--accent-color); stroke-width: 16; stroke-linecap: round; transition: stroke-dashoffset 1.5s cubic-bezier(0.4, 0, 0.2, 1); filter: drop-shadow(0 0 6px var(--accent-glow)); }
    .ring-burned { fill: none; stroke: #FF9800; stroke-width: 16; stroke-linecap: round; transition: stroke-dashoffset 1.5s cubic-bezier(0.4, 0, 0.2, 1); filter: drop-shadow(0 0 6px rgba(255, 152, 0, 0.4)); }"""
content = content.replace(ring_css_target, ring_css_replacement)


# 3. Add Profile Button back to fix JS Crash
# We will add it under the Calendar button
alarm_div_target = """      <div style="display: flex; gap: 12px; align-items: center;">
        <input type="time" id="reminder-time" value="18:30" style="flex: 1; padding: 12px; border-radius: 8px; border: 1px solid var(--surface-border); background: var(--bg-color); color: var(--text-color);">
        <button id="add-to-calendar-btn" class="primary-btn" style="flex: 2; margin: 0; display: flex; justify-content: center; align-items: center; gap: 8px;">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
          Takvime Ekle
        </button>
      </div>
    </div>"""

alarm_div_replacement = """      <div style="display: flex; gap: 12px; align-items: center;">
        <input type="time" id="reminder-time" value="18:30" style="flex: 1; padding: 12px; border-radius: 8px; border: 1px solid var(--surface-border); background: var(--bg-color); color: var(--text-color);">
        <button id="add-to-calendar-btn" class="primary-btn" style="flex: 2; margin: 0; display: flex; justify-content: center; align-items: center; gap: 8px;">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
          Takvime Ekle
        </button>
      </div>
      <button type="button" id="profile-modal-btn" class="secondary-btn" style="margin-top: 16px; font-size: 0.9rem;">Ayarlar ve Profili Düzenle</button>
    </div>"""
content = content.replace(alarm_div_target, alarm_div_replacement)


# 4. Initialize Ring Dashoffset before UpdateUI so animation happens
init_target = """    function init() {
      loadState();
      checkOnboarding();
      checkMidnightReset();
      updateUI();
      setupEventListeners();
    }"""
init_replacement = """    function init() {
      el.ring.style.strokeDasharray = RING_CIRCUMFERENCE;
      el.ring.style.strokeDashoffset = RING_CIRCUMFERENCE;
      el.ringBurned.style.strokeDasharray = RING_CIRCUMFERENCE;
      el.ringBurned.style.strokeDashoffset = RING_CIRCUMFERENCE;
      
      loadState();
      checkOnboarding();
      checkMidnightReset();
      setTimeout(updateUI, 50); // slight delay to trigger CSS transition gliding
      setupEventListeners();
    }"""
content = content.replace(init_target, init_replacement)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Final UI polished and bugs fixed!")
