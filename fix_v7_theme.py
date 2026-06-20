import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix CSS
css_target = """    .dashboard-container { padding-bottom: 40px; }
    .meal-dash-btn { 
      background: var(--surface-color); border: 1px solid var(--surface-border); border-radius: 16px; 
      padding: 16px; color: var(--text-color); font-family: var(--font-heading); font-weight: 700; font-size: 1.1rem;
      text-transform: uppercase; letter-spacing: 1px; cursor: pointer; transition: all 0.2s;
      display: flex; justify-content: space-between; align-items: center; backdrop-filter: blur(24px);
    }
    .meal-dash-btn:hover { background: rgba(0, 169, 143, 0.1); border-color: var(--accent-color); }
    .meal-dash-cal { color: var(--accent-color); font-size: 0.9rem; font-weight: 700; }"""

css_replace = """    .dashboard-container { padding-bottom: 40px; }
    .meal-dash-btn { 
      background: transparent; border: none; border-bottom: 1px solid var(--surface-border);
      border-radius: 0; padding: 14px 4px; color: var(--text-color); font-family: var(--font-body); font-weight: 500; font-size: 1rem;
      cursor: pointer; transition: all 0.3s ease; display: flex; justify-content: space-between; align-items: center;
    }
    .meal-dash-btn:last-child { border-bottom: none; }
    .meal-dash-btn:hover { padding-left: 8px; color: var(--accent-color); }
    .meal-dash-cal { color: var(--text-muted); font-size: 0.9rem; font-weight: 400; transition: color 0.3s; }
    .meal-dash-btn:hover .meal-dash-cal { color: var(--accent-color); }"""

content = content.replace(css_target, css_replace)

# Fix Top Section HTML
top_section_target = """    <!-- Top Section: Ring + Meals -->
    <div style="display: flex; gap: 16px; margin-bottom: 24px;">
      <!-- Left: Ring -->
      <div class="glass-card" style="flex: 1; margin: 0; padding: 16px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
        <div class="ring-container" style="margin: 0; width: 100%; max-width: 150px; aspect-ratio: 1/1;">
          <svg class="calorie-ring-svg" viewBox="0 0 220 220">
            <circle class="ring-bg" cx="110" cy="110" r="104"></circle>
            <circle class="ring-burned" id="calorie-ring-burned" cx="110" cy="110" r="104"></circle>
            <circle class="ring-progress" id="calorie-ring" cx="110" cy="110" r="104"></circle>
          </svg>
          <div class="calories-info">
            <div class="main-cal">
              <span id="calories-consumed-main">0</span>
              <span style="font-size: 1rem; color: var(--text-muted);">kcal</span>
            </div>
            <div style="font-size: 0.8rem; color: var(--text-muted); margin-top: 4px;">Hedef: <span id="calories-goal">2000</span></div>
          </div>
        </div>
        <p id="goal-exceeded-msg" class="info-text" style="color: var(--error-color); text-align: center; display: none; margin-top: 12px;">Hedef aşıldı!</p>
      </div>

      <!-- Right: Meal Stack -->
      <div style="flex: 1; display: flex; flex-direction: column; gap: 10px;">
        <button class="meal-dash-btn" data-category="breakfast">
          KAHVALTI <span id="cal-breakfast" class="meal-dash-cal">0 kcal</span>
        </button>
        <button class="meal-dash-btn" data-category="lunch">
          ÖĞLE <span id="cal-lunch" class="meal-dash-cal">0 kcal</span>
        </button>
        <button class="meal-dash-btn" data-category="dinner">
          AKŞAM <span id="cal-dinner" class="meal-dash-cal">0 kcal</span>
        </button>
        <button class="meal-dash-btn" data-category="snack">
          EK <span id="cal-snack" class="meal-dash-cal">0 kcal</span>
        </button>
      </div>
    </div>"""

top_section_replace = """    <!-- Top Section: Ring + Meals -->
    <div class="glass-card" style="display: flex; gap: 24px; align-items: center; padding: 24px 20px;">
      <!-- Left: Ring -->
      <div style="flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center;">
        <div class="ring-container" style="margin: 0; width: 100%; max-width: 140px; aspect-ratio: 1/1;">
          <svg class="calorie-ring-svg" viewBox="0 0 220 220">
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
        </div>
        <p id="goal-exceeded-msg" class="info-text" style="color: var(--error-color); text-align: center; display: none; margin-top: 12px; font-size: 0.85rem;">Hedef aşıldı!</p>
      </div>

      <!-- Right: Meal Stack -->
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
      </div>
    </div>"""
content = content.replace(top_section_target, top_section_replace)

# Fix Middle Section HTML
middle_target = """    <!-- Middle Section: Exercise & GPS -->
    <div class="glass-card">
      <h2 class="section-title">Egzersiz & GPS</h2>
      <div class="input-group">
        <select id="activity-type" style="width: 100%; padding: 12px; border-radius: 8px; border: 1px solid var(--surface-border); background: var(--bg-color); color: var(--text-color); margin-bottom: 12px; font-family: var(--font-body);">
          <option value="walk">🏃‍♂️ Yürüyüş</option>
          <option value="run">🏃‍♀️ Koşu</option>
          <option value="bike">🚴 Bisiklet</option>
        </select>
      </div>"""

middle_replace = """    <!-- Middle Section: Exercise & GPS -->
    <div class="glass-card">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
        <h2 class="section-title" style="margin: 0; font-size: 1.2rem;">Egzersiz ve GPS</h2>
        <select id="activity-type" style="padding: 6px 12px; border-radius: 20px; border: 1px solid var(--surface-border); background: var(--surface-color); color: var(--text-color); font-family: var(--font-body); font-size: 0.9rem; outline: none; -webkit-appearance: none; cursor: pointer;">
          <option value="walk">Yürüyüş</option>
          <option value="run">Koşu</option>
          <option value="bike">Bisiklet</option>
        </select>
      </div>"""
content = content.replace(middle_target, middle_replace)


# Remove the unit 'kcal' setting in updateUI since the button design now has it cleaner
# JS target:
js_cal_target = """      Object.keys(categoryTotals).forEach(cat => {
        if(el.cals[cat]) el.cals[cat].textContent = categoryTotals[cat] + ' kcal';
      });"""
js_cal_replace = """      Object.keys(categoryTotals).forEach(cat => {
        if(el.cals[cat]) el.cals[cat].textContent = categoryTotals[cat];
      });"""
content = content.replace(js_cal_target, js_cal_replace)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("V7 Theme elegantly simplified.")
