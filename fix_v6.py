import re
import shutil
import os

# Move logo to project folder
logo_src = "/Users/kedi/.gemini/antigravity-ide/brain/4343f88a-4284-4c23-922c-edc7fd6ab242/metra_logo_1781974681812.png"
logo_dest = "/Users/kedi/Desktop/Antigravity/Spor app/metra_logo.png"
if os.path.exists(logo_src):
    shutil.copy(logo_src, logo_dest)

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. CSS Theme to Liquid Glass
css_theme_target = """:root {
      --font-heading: 'DM Sans', sans-serif;
      --font-body: 'Inter', sans-serif;
    }

    [data-theme="light"] {
      --bg-color: #f4f6f8;
      --surface-color: rgba(255, 255, 255, 0.85);
      --surface-border: rgba(0, 0, 0, 0.08);
      --accent-color: #00C49F; /* Slightly darker mint for white bg */
      --accent-glow: rgba(0, 196, 159, 0.3);
      --text-color: #1a1f2b;
      --text-muted: #64748b;
      --error-color: #ef4444;
      --gradient-bg: radial-gradient(circle at top right, #ffffff 0%, var(--bg-color) 100%);
      --ring-bg: rgba(0,0,0,0.05);
    }

    [data-theme="dark"] {
      --bg-color: #0b0f19;
      --surface-color: rgba(26, 32, 53, 0.7);
      --surface-border: rgba(255, 255, 255, 0.05);
      --accent-color: #00F5C3;
      --accent-glow: rgba(0, 245, 195, 0.4);
      --text-color: #ffffff;
      --text-muted: #8b9bb4;
      --error-color: #FF4D4D;
      --gradient-bg: radial-gradient(circle at top right, #112236 0%, var(--bg-color) 60%);
      --ring-bg: rgba(255,255,255,0.05);
    }"""

css_theme_replacement = """:root {
      --font-heading: 'DM Sans', sans-serif;
      --font-body: 'Inter', sans-serif;
    }

    [data-theme="light"] {
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
content = content.replace(css_theme_target, css_theme_replacement)

# Liquid Glass Card CSS Update
glass_card_target = """    .glass-card {
      background: var(--surface-color);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid var(--surface-border);
      border-radius: 20px;
      padding: 20px;
      margin-bottom: 24px;
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
    }"""
glass_card_replacement = """    .glass-card {
      background: var(--surface-color);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      border: 1px solid var(--surface-border);
      border-radius: 24px;
      padding: 20px;
      margin-bottom: 24px;
      box-shadow: var(--glass-shadow);
      position: relative;
      overflow: hidden;
    }
    .glass-card::before {
      content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
      background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 100%);
      pointer-events: none; border-radius: 24px;
    }"""
content = content.replace(glass_card_target, glass_card_replacement)

# Update the Header for METRA Rebrand & SVG Icons
header_target_pattern = r'<header style="position: relative;">.*?</header>'
svg_sun = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>'
svg_bell = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path><path d="M13.73 21a2 2 0 0 1-3.46 0"></path></svg>'
svg_plus = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>'

header_replacement = f"""  <header style="position: relative; display: flex; align-items: center; justify-content: center; margin-bottom: 24px; min-height: 60px;">
    <button id="reminder-modal-btn" class="theme-toggle" style="position: absolute; left: 0; color: var(--text-color);">{svg_bell}</button>
    <div style="text-align: center; z-index: 1;">
      <img src="metra_logo.png" alt="METRA Logo" style="width: 48px; height: 48px; border-radius: 12px; margin-bottom: 8px; box-shadow: 0 4px 12px rgba(0,245,195,0.3);">
      <h1 style="font-size: 1.5rem; letter-spacing: 3px; font-weight: 800; background: linear-gradient(90deg, var(--text-color), var(--accent-color)); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">METRA</h1>
    </div>
    <button id="theme-toggle-btn" class="theme-toggle" style="position: absolute; right: 0; color: var(--text-color);">
      <div id="theme-icon-container">{svg_sun}</div>
    </button>
  </header>"""
content = re.sub(header_target_pattern, header_replacement, content, flags=re.DOTALL)

# Re-inject the Meal Cards to #tab-home
meal_cards_html = f"""
      <div class="glass-card meal-category-card" style="z-index: 10;">
        <div class="meal-header">
          <h2 class="section-title" style="margin-bottom: 0;">Kahvaltı</h2>
          <div class="meal-header-right">
            <span id="cal-breakfast" class="category-cal">0</span>
            <button class="add-meal-btn" data-category="breakfast" style="color: var(--accent-color); background: transparent; border: 1px solid var(--surface-border);">{svg_plus}</button>
          </div>
        </div>
        <ul id="list-breakfast" class="meal-list"></ul>
      </div>

      <div class="glass-card meal-category-card" style="z-index: 9;">
        <div class="meal-header">
          <h2 class="section-title" style="margin-bottom: 0;">Öğle Yemeği</h2>
          <div class="meal-header-right">
            <span id="cal-lunch" class="category-cal">0</span>
            <button class="add-meal-btn" data-category="lunch" style="color: var(--accent-color); background: transparent; border: 1px solid var(--surface-border);">{svg_plus}</button>
          </div>
        </div>
        <ul id="list-lunch" class="meal-list"></ul>
      </div>

      <div class="glass-card meal-category-card" style="z-index: 8;">
        <div class="meal-header">
          <h2 class="section-title" style="margin-bottom: 0;">Akşam Yemeği</h2>
          <div class="meal-header-right">
            <span id="cal-dinner" class="category-cal">0</span>
            <button class="add-meal-btn" data-category="dinner" style="color: var(--accent-color); background: transparent; border: 1px solid var(--surface-border);">{svg_plus}</button>
          </div>
        </div>
        <ul id="list-dinner" class="meal-list"></ul>
      </div>

      <div class="glass-card meal-category-card" style="margin-bottom: 32px; z-index: 7;">
        <div class="meal-header">
          <h2 class="section-title" style="margin-bottom: 0;">Ara Öğünler</h2>
          <div class="meal-header-right">
            <span id="cal-snack" class="category-cal">0</span>
            <button class="add-meal-btn" data-category="snack" style="color: var(--accent-color); background: transparent; border: 1px solid var(--surface-border);">{svg_plus}</button>
          </div>
        </div>
        <ul id="list-snack" class="meal-list"></ul>
      </div>
"""

# Insert meal cards right after the daily calorie summary glass-card in tab-home
# Find the end of the goal-exceeded-msg block
goal_exceed_idx = content.find('<div class="info-text" id="goal-exceeded-msg" style="color: var(--error-color); margin-top: 12px; display: none;">Hedefini aştın!</div>\n      </div>')
if goal_exceed_idx != -1:
    insert_pos = goal_exceed_idx + len('<div class="info-text" id="goal-exceeded-msg" style="color: var(--error-color); margin-top: 12px; display: none;">Hedefini aştın!</div>\n      </div>')
    content = content[:insert_pos] + "\n" + meal_cards_html + content[insert_pos:]
else:
    print("Could not find insertion point for meal cards!")

# Change Theme toggle JS to swap SVG
js_theme_target = """      el.themeToggleBtn.textContent = currentTheme === 'light' ? '🌙' : '☀️';

      el.themeToggleBtn.addEventListener('click', () => {
        currentTheme = currentTheme === 'light' ? 'dark' : 'light';
        document.body.setAttribute('data-theme', currentTheme);
        el.themeToggleBtn.textContent = currentTheme === 'light' ? '🌙' : '☀️';"""

svg_moon = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>'
js_theme_replacement = f"""      const themeIconContainer = document.getElementById('theme-icon-container');
      themeIconContainer.innerHTML = currentTheme === 'light' ? '{svg_moon}' : '{svg_sun}';

      el.themeToggleBtn.addEventListener('click', () => {{
        currentTheme = currentTheme === 'light' ? 'dark' : 'light';
        document.body.setAttribute('data-theme', currentTheme);
        themeIconContainer.innerHTML = currentTheme === 'light' ? '{svg_moon}' : '{svg_sun}';"""
content = content.replace(js_theme_target, js_theme_replacement)


# Also ensure that `el` has the correct `addMealBtn` logic bound to `body` if dynamic, 
# but `document.querySelectorAll('.add-meal-btn').forEach` runs in `setupEventListeners`
# So they will bind properly if the HTML exists before `setupEventListeners` runs (which it does).
# But wait, `el` has `addMealBtn` ? No, `el` doesn't store them, it uses `document.querySelectorAll` directly. This is correct.

# Remove the Emojis from Modal titles
content = content.replace("<h2>⚙️ Ayarlar</h2>", "<h2>Ayarlar</h2>")
content = content.replace("<h2>🏆 Uygulama Bilgileri</h2>", "<h2>Uygulama Bilgileri</h2>")
content = content.replace("<h2>👟 Yürüyüş & Egzersiz</h2>", "<h2>Yürüyüş & Egzersiz</h2>")
content = content.replace(">🔔 Hatırlatıcı Ayarları</h2>", ">Hatırlatıcı Ayarları</h2>")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("V6 (METRA & Liquid Glass) successfully deployed!")
