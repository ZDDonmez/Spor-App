import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. CSS Theme to Opaque Solid Theme
css_theme_target = """    [data-theme="light"] {
      --bg-color: #e2e8f0;
      --surface-color: rgba(255, 255, 255, 0.4);
      --surface-border: rgba(255, 255, 255, 0.6);
      --accent-color: #00A98F;
      --accent-glow: rgba(0, 169, 143, 0.4);
      --text-color: #0f172a;
      --text-muted: #475569;
      --error-color: #ef4444;
      --gradient-bg: radial-gradient(circle at top right, #f8fafc 0%, var(--bg-color) 100%);
      --ring-bg: rgba(0,0,0,0.05);
      --glass-shadow: 0 8px 32px rgba(31, 38, 135, 0.1);
    }

    [data-theme="dark"] {
      --bg-color: #050b14;
      --surface-color: rgba(16, 24, 40, 0.4);
      --surface-border: rgba(255, 255, 255, 0.1);
      --accent-color: #00F5C3;
      --accent-glow: rgba(0, 245, 195, 0.5);
      --text-color: #f8fafc;
      --text-muted: #94a3b8;
      --error-color: #FF4D4D;
      --gradient-bg: radial-gradient(circle at top right, #0d1b2a 0%, var(--bg-color) 80%);
      --ring-bg: rgba(255,255,255,0.05);
      --glass-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
    }"""

css_theme_replacement = """    [data-theme="light"] {
      --bg-color: #f4f6f8;
      --surface-color: #ffffff;
      --surface-border: #e2e8f0;
      --accent-color: #00A98F;
      --accent-glow: rgba(0, 169, 143, 0.2);
      --text-color: #1e293b;
      --text-muted: #64748b;
      --error-color: #ef4444;
      --gradient-bg: var(--bg-color);
      --ring-bg: #e2e8f0;
      --glass-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    }

    [data-theme="dark"] {
      --bg-color: #0f172a;
      --surface-color: #1e293b;
      --surface-border: #334155;
      --accent-color: #00F5C3;
      --accent-glow: rgba(0, 245, 195, 0.2);
      --text-color: #f8fafc;
      --text-muted: #94a3b8;
      --error-color: #ef4444;
      --gradient-bg: var(--bg-color);
      --ring-bg: #334155;
      --glass-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    }"""
content = content.replace(css_theme_target, css_theme_replacement)

# 2. Fix Glass Card (Remove blur, keep solid)
glass_card_target = """    .glass-card {
      background: var(--surface-color);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      border: 1px solid rgba(255, 255, 255, 0.2);
      border-radius: 32px;
      padding: 24px;
      margin-bottom: 24px;
      box-shadow: var(--glass-shadow);
      position: relative;
      overflow: hidden;
    }
    .glass-card::before {
      content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
      background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 100%);
      pointer-events: none; border-radius: 32px;
    }"""

glass_card_replacement = """    .glass-card {
      background: var(--surface-color);
      border: 1px solid var(--surface-border);
      border-radius: 20px;
      padding: 20px;
      margin-bottom: 24px;
      box-shadow: var(--glass-shadow);
      position: relative;
      overflow: hidden;
    }"""
content = content.replace(glass_card_target, glass_card_replacement)


# 3. Fix Meal Dash Buttons (Make them rounded pills/cards instead of bottom-border lines)
meal_btn_target = """    .meal-dash-btn { 
      background: transparent; border: none; border-bottom: 1px solid var(--surface-border);
      border-radius: 0; padding: 14px 4px; color: var(--text-color); font-family: var(--font-body); font-weight: 500; font-size: 1rem;
      cursor: pointer; transition: all 0.3s ease; display: flex; justify-content: space-between; align-items: center;
    }
    .meal-dash-btn:last-child { border-bottom: none; }
    .meal-dash-btn:hover { padding-left: 8px; color: var(--accent-color); }"""

meal_btn_replacement = """    .meal-dash-btn { 
      background: var(--bg-color); border: 1px solid var(--surface-border);
      border-radius: 12px; padding: 12px 16px; color: var(--text-color); font-family: var(--font-body); font-weight: 600; font-size: 0.95rem;
      cursor: pointer; transition: all 0.2s ease; display: flex; justify-content: space-between; align-items: center;
      box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    .meal-dash-btn:hover { border-color: var(--accent-color); color: var(--accent-color); transform: translateY(-1px); box-shadow: 0 4px 8px rgba(0,0,0,0.05); }"""
content = content.replace(meal_btn_target, meal_btn_replacement)


# 4. Remove Profile Icon from Header
profile_icon_pattern = r'    <button id="profile-modal-btn" class="theme-toggle".*?</button>'
content = re.sub(profile_icon_pattern, '', content, flags=re.DOTALL)


# 5. Fix Ring Container to position the text INSIDE the ring absolute center
ring_html_target = """        <div class="ring-container" style="margin: 0; width: 100%; max-width: 140px; aspect-ratio: 1/1;">
          <svg class="ring-svg" viewBox="0 0 220 220">
            <circle class="ring-bg" cx="110" cy="110" r="104"></circle>
            <circle class="ring-burned" id="calorie-ring-burned" cx="110" cy="110" r="104"></circle>
            <circle class="ring-progress" id="calorie-ring" cx="110" cy="110" r="104"></circle>
          </svg>
          <div class="calories-info">
            <div class="main-cal">
              <span id="calories-consumed-main">0</span>
            </div>
            <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 2px;">Kcal</div>
            <div style="font-size: 0.75rem; color: var(--text-muted); opacity: 0.6; margin-top: 2px;">Hedef: <span id="calories-goal">2000</span></div>
          </div>
        </div>"""

ring_html_replacement = """        <div class="ring-container" style="position: relative; margin: 0; width: 100%; max-width: 140px; aspect-ratio: 1/1; display: flex; justify-content: center; align-items: center;">
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
content = content.replace(ring_html_target, ring_html_replacement)

# Make sure CSS has position logic for the ring and info text correctly
# .ring-svg css block:
ring_css_target = """    /* Calorie Ring */
    .ring-container { position: relative; width: 220px; height: 220px; margin: 0 auto 24px; }
    .ring-svg { width: 100%; height: 100%; transform: rotate(-90deg); }"""

ring_css_replacement = """    /* Calorie Ring */
    .ring-container { position: relative; width: 220px; height: 220px; margin: 0 auto 24px; }
    .ring-svg { width: 100%; height: 100%; transform: rotate(-90deg); }
    .calories-info { display: flex; flex-direction: column; align-items: center; justify-content: center; }"""
content = content.replace(ring_css_target, ring_css_replacement)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Opaque theme applied and bugs fixed!")
