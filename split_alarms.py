import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update HTML for Alarms
alarm_target = """    <div class="glass-card" style="margin-bottom: 0;">
      <h2 class="section-title" style="margin: 0 0 12px 0;">Spor Hatırlatıcı Alarm</h2>
      <p class="info-text" style="margin-bottom: 16px;">Her gün antrenman veya su içme vakti geldiğinde telefonunun çalması için takvime ekle.</p>
      
      <div style="display: flex; gap: 12px; align-items: center;">
        <input type="time" id="reminder-time" value="18:30" style="flex: 1; padding: 12px; border-radius: 8px; border: 1px solid var(--surface-border); background: var(--bg-color); color: var(--text-color);">
        <button id="add-to-calendar-btn" class="primary-btn" style="flex: 2; margin: 0; display: flex; justify-content: center; align-items: center; gap: 8px;">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
          Takvime Ekle
        </button>
      </div>
      <button type="button" id="profile-modal-btn" class="secondary-btn" style="margin-top: 16px; font-size: 0.9rem;">Ayarlar ve Profili Düzenle</button>
    </div>"""

alarm_replacement = """    <div class="glass-card" style="margin-bottom: 0; border: none; background: transparent; padding: 0; box-shadow: none;">
      <div style="display: flex; gap: 12px;">
        
        <!-- Left Box: Water Alarm -->
        <div style="flex: 1; background: var(--surface-color); border: 1px solid var(--surface-border); border-radius: 16px; padding: 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <h3 style="font-size: 1rem; margin-bottom: 6px; color: #0ea5e9; font-family: var(--font-heading); display: flex; align-items: center; gap: 6px;">💧 Su Hatırlatıcı</h3>
            <p style="font-size: 0.75rem; color: var(--text-muted); margin-bottom: 12px; line-height: 1.3;">Gün boyu ara ara su içmeni hatırlatır.</p>
          </div>
          <button id="add-water-alarm-btn" style="background: rgba(14, 165, 233, 0.1); border: 1px solid #0ea5e9; color: #0ea5e9; padding: 10px; border-radius: 10px; font-size: 0.85rem; font-weight: 600; width: 100%; cursor: pointer;">Takvime Ekle</button>
        </div>

        <!-- Right Box: Sports Alarm -->
        <div style="flex: 1; background: var(--surface-color); border: 1px solid var(--surface-border); border-radius: 16px; padding: 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <h3 style="font-size: 1rem; margin-bottom: 6px; color: var(--text-color); font-family: var(--font-heading); display: flex; align-items: center; gap: 6px;">🏃‍♂️ Spor Alarmı</h3>
            <input type="time" id="reminder-time" value="18:30" style="width: 100%; padding: 8px; border-radius: 8px; border: 1px solid var(--surface-border); background: var(--bg-color); color: var(--text-color); margin-bottom: 12px; font-size: 0.9rem; font-family: var(--font-body); outline: none;">
          </div>
          <button id="add-to-calendar-btn" style="background: var(--accent-color); color: #fff; padding: 10px; border-radius: 10px; font-size: 0.85rem; font-weight: 600; border: none; width: 100%; cursor: pointer; text-shadow: 0 1px 2px rgba(0,0,0,0.2);">Takvime Ekle</button>
        </div>

      </div>
      <button type="button" id="profile-modal-btn" class="secondary-btn" style="margin-top: 16px; font-size: 0.9rem; background: var(--surface-color);">Ayarlar ve Profili Düzenle</button>
    </div>"""

content = content.replace(alarm_target, alarm_replacement)


# 2. Add Water Alarm logic to JS
js_calendar_target = """      el.addToCalendarBtn.addEventListener('click', () => {
        const timeVal = el.reminderTime.value;"""

js_calendar_replacement = """      document.getElementById('add-water-alarm-btn').addEventListener('click', () => {
        const now = new Date();
        now.setHours(now.getHours() + 1);
        const startTime = now.toISOString().replace(/-|:|\.\\d+/g, '');
        const endTime = new Date(now.getTime() + 15*60000).toISOString().replace(/-|:|\.\\d+/g, '');
        
        const icsContent = `BEGIN:VCALENDAR\\nVERSION:2.0\\nBEGIN:VEVENT\\nDTSTART:${startTime}\\nDTEND:${endTime}\\nRRULE:FREQ=HOURLY;INTERVAL=2\\nSUMMARY:💧 Su İçme Vakti!\\nDESCRIPTION:Vücudunu susuz bırakma. Bir bardak su iç!\\nBEGIN:VALARM\\nTRIGGER:-PT0M\\nACTION:DISPLAY\\nDESCRIPTION:Reminder\\nEND:VALARM\\nEND:VEVENT\\nEND:VCALENDAR`;
        
        const blob = new Blob([icsContent], { type: 'text/calendar;charset=utf-8' });
        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = 'su_hatirlatici.ics';
        link.click();
        showToast('Su alarmı indirildi! Tıklayıp kurabilirsin.');
      });

      el.addToCalendarBtn.addEventListener('click', () => {
        const timeVal = el.reminderTime.value;"""

content = content.replace(js_calendar_target, js_calendar_replacement)


# 3. Force Light Theme Once
js_theme_target = """      let currentTheme = localStorage.getItem('antigravity_theme') || 'light';"""
js_theme_replacement = """      if (!localStorage.getItem('v9_theme_reset')) {
        localStorage.setItem('antigravity_theme', 'light');
        localStorage.setItem('v9_theme_reset', 'true');
      }
      let currentTheme = localStorage.getItem('antigravity_theme') || 'light';"""
content = content.replace(js_theme_target, js_theme_replacement)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Alarms split and theme reset applied!")
