import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix the syntax error leftover
content = content.replace('\n    ">`).join(\'\');\n    }\n', '')
content = content.replace('\n    ">`).join(\'\');\n    }', '')

# 2. Add Reminder button to header
header_target = """  <header style="position: relative;">
    <h1>Antigravity</h1>
    <p>Günlük Kalori ve Aktivite Asistanı</p>
    <button id="theme-toggle-btn" class="theme-toggle">☀️</button>
  </header>"""

header_replacement = """  <header style="position: relative;">
    <button id="reminder-modal-btn" class="theme-toggle" style="left: 20px; right: auto;">🔔</button>
    <h1>Antigravity</h1>
    <p>Günlük Kalori ve Aktivite Asistanı</p>
    <button id="theme-toggle-btn" class="theme-toggle">☀️</button>
  </header>"""
content = content.replace(header_target, header_replacement)

# 3. Remove the inline reminder-widget
reminder_widget_pattern = r'        <div class="glass-card" id="reminder-widget" style="margin-bottom: 16px; padding: 12px 16px;">.*?</div>\s*</div>\s*</div>'
content = re.sub(reminder_widget_pattern, '', content, flags=re.DOTALL)

# Let's be sure to also remove it if the regex failed:
reminder_hard_string = """        <div class="glass-card" id="reminder-widget" style="margin-bottom: 16px; padding: 12px 16px;">
          <div class="toggle-container" style="margin-bottom: 8px;">
            <div>
              <label style="margin: 0; color: var(--text-color); font-size: 1rem;">🔔 Antrenman & Su</label>
              <div class="info-text">Hatırlatıcı açık/kapalı</div>
            </div>
            <label class="switch">
              <input type="checkbox" id="reminder-toggle">
              <span class="slider"></span>
            </label>
          </div>
          <div id="reminder-settings" style="opacity: 0.5; pointer-events: none; transition: opacity 0.3s; display: flex; gap: 8px; align-items: center;">
            <input type="time" id="reminder-time" value="18:30" style="flex: 2; padding: 8px;">
            <button type="button" id="save-reminder-btn" class="secondary-btn" style="flex: 1; padding: 8px; margin: 0;">Kaydet</button>
          </div>
        </div>"""
content = content.replace(reminder_hard_string, '')

# 4. Add the Reminder Modal
modal_html = """
  <!-- Reminder Modal -->
  <div id="reminder-modal" class="overlay hidden" style="justify-content: flex-start; padding: 80px 20px 20px 20px; background: rgba(0,0,0,0.6);">
    <div class="glass-card" style="animation: fadeSlideUp 0.3s ease;">
      <h2 class="section-title" style="color: var(--accent-color);">🔔 Hatırlatıcı Ayarları</h2>
      
      <div class="toggle-container" style="margin-bottom: 16px;">
        <div>
          <label style="margin: 0; color: var(--text-color); font-size: 1rem;">Hatırlatıcıyı Aç</label>
          <div class="info-text">Günlük aktivite/su hatırlatması</div>
        </div>
        <label class="switch">
          <input type="checkbox" id="reminder-toggle">
          <span class="slider"></span>
        </label>
      </div>

      <div id="reminder-settings" style="opacity: 0.5; pointer-events: none; transition: opacity 0.3s;">
        <div class="input-group">
          <label for="reminder-time">Hatırlatma Saati</label>
          <input type="time" id="reminder-time" value="18:30">
        </div>
        <button type="button" id="save-reminder-btn" class="secondary-btn">Kaydet</button>
      </div>
      
      <button type="button" id="close-reminder-modal" class="secondary-btn" style="margin-top: 12px; border: none;">Kapat</button>
    </div>
  </div>
"""
modal_insert_idx = content.find('  <!-- Add Meal Modal -->')
content = content[:modal_insert_idx] + modal_html + content[modal_insert_idx:]

# 5. Update JS elements and listeners
el_replace = """      reminderModalBtn: document.getElementById('reminder-modal-btn'),
      reminderModal: document.getElementById('reminder-modal'),
      closeReminderModal: document.getElementById('close-reminder-modal'),
      reminderToggle:"""
content = content.replace("      reminderToggle:", el_replace)

js_listeners = """      el.reminderModalBtn.addEventListener('click', () => {
        el.reminderModal.classList.remove('hidden');
      });
      el.closeReminderModal.addEventListener('click', () => {
        el.reminderModal.classList.add('hidden');
      });

      el.reminderToggle.addEventListener('change', (e) => {"""
content = content.replace("      el.reminderToggle.addEventListener('change', (e) => {", js_listeners)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Bug fixed and Reminder moved to top-left modal")
