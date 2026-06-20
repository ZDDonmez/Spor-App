import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add CSS for switch toggle
css_target = """    .tab-content { display: none; animation: fadeSlideUp 0.4s ease forwards; }"""
css_replacement = """    /* Switch Toggle */
    .switch { position: relative; display: inline-block; width: 44px; height: 24px; }
    .switch input { opacity: 0; width: 0; height: 0; }
    .slider { position: absolute; cursor: pointer; top: 0; left: 0; right: 0; bottom: 0; background-color: var(--surface-border); transition: .4s; border-radius: 24px; }
    .slider:before { position: absolute; content: ""; height: 18px; width: 18px; left: 3px; bottom: 3px; background-color: white; transition: .4s; border-radius: 50%; box-shadow: 0 2px 4px rgba(0,0,0,0.2); }
    input:checked + .slider { background-color: #0ea5e9; }
    input:checked + .slider:before { transform: translateX(20px); }

    .tab-content { display: none; animation: fadeSlideUp 0.4s ease forwards; }"""
content = content.replace(css_target, css_replacement)

# 2. Add profile button to header
header_target = """  <header style="position: relative; display: flex; align-items: center; justify-content: center; margin-bottom: 12px; min-height: 48px; padding: 12px 0 0 0;">

    <div style="text-align: center; z-index: 1;">"""
header_replacement = """  <header style="position: relative; display: flex; align-items: center; justify-content: center; margin-bottom: 12px; min-height: 48px; padding: 12px 0 0 0;">
    <button id="profile-modal-btn" class="theme-toggle" style="position: absolute; left: 16px; color: var(--text-color); cursor: pointer; background: transparent; border: none; padding: 0;">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
    </button>
    <div style="text-align: center; z-index: 1;">"""
content = content.replace(header_target, header_replacement)

# 3. Remove old profile button
old_prof_target = """      <button type="button" id="profile-modal-btn" class="secondary-btn" style="margin-top: 16px; font-size: 0.9rem;">Ayarlar ve Profili Düzenle</button>
    </div>"""
content = content.replace(old_prof_target, """    </div>""")
content = content.replace('<button type="button" id="profile-modal-btn" class="secondary-btn" style="margin-top: 16px; font-size: 0.9rem; background: var(--surface-color);">Ayarlar ve Profili Düzenle</button>', '')


# 4. Replace water button with toggle
water_target = """          <button id="add-water-alarm-btn" style="background: rgba(14, 165, 233, 0.1); border: 1px solid #0ea5e9; color: #0ea5e9; padding: 10px; border-radius: 10px; font-size: 0.85rem; font-weight: 600; width: 100%; cursor: pointer;">Takvime Ekle</button>"""
water_replacement = """          <div style="display: flex; align-items: center; justify-content: space-between; margin-top: 4px; padding: 8px 12px; background: rgba(14, 165, 233, 0.05); border-radius: 12px; border: 1px solid rgba(14, 165, 233, 0.2);">
            <span style="font-size: 0.85rem; color: #0ea5e9; font-weight: 600;">Otomatik Bildirim</span>
            <label class="switch">
              <input type="checkbox" id="water-alarm-toggle">
              <span class="slider"></span>
            </label>
          </div>"""
content = content.replace(water_target, water_replacement)

# 5. Add Water Prompt Modal
modal_insertion = """  <!-- Water Prompt Modal -->
  <div id="water-prompt-modal" class="overlay hidden" style="justify-content: center; align-items: center; padding: 20px; z-index: 9999;">
    <div class="glass-card" style="width: 100%; max-width: 350px; text-align: center; border: 1px solid #0ea5e9; box-shadow: 0 0 30px rgba(14, 165, 233, 0.2);">
      <h2 class="section-title" style="color: #0ea5e9; justify-content: center; font-size: 1.5rem; margin-bottom: 12px;">💧 Su İçtin mi?</h2>
      <p style="color: var(--text-color); margin-bottom: 24px;">Son bildirimden bu yana hiç su içtin mi? Vücudunu susuz bırakmamalısın!</p>
      <div style="display: flex; gap: 12px;">
        <button id="water-no-btn" style="flex: 1; padding: 12px; border-radius: 12px; border: 1px solid var(--error-color); background: transparent; color: var(--error-color); font-weight: 600; cursor: pointer;">Hayır, İçmedim</button>
        <button id="water-yes-btn" style="flex: 1; padding: 12px; border-radius: 12px; border: none; background: #0ea5e9; color: #fff; font-weight: 600; cursor: pointer;">Evet, İçtim!</button>
      </div>
    </div>
  </div>"""

content = content.replace('  <!-- Profile Setup Modal -->', modal_insertion + '\n\n  <!-- Profile Setup Modal -->')

# 6. Update JS logic
js_target = """      document.getElementById('add-water-alarm-btn').addEventListener('click', () => {
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
      });"""

js_replacement = """      let waterIntervalId = null;
      const waterToggle = document.getElementById('water-alarm-toggle');
      
      const startWaterInterval = (durationMs) => {
        if(waterIntervalId) clearInterval(waterIntervalId);
        waterIntervalId = setInterval(() => {
          if (Notification.permission === 'granted') {
            const notif = new Notification("💧 Su Vakti!", {
              body: "Bir bardak su içtin mi? Tıklayarak cevapla!",
              icon: "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>💧</text></svg>"
            });
            notif.onclick = () => {
              window.focus();
              document.getElementById('water-prompt-modal').classList.remove('hidden');
              notif.close();
            };
          } else {
            document.getElementById('water-prompt-modal').classList.remove('hidden');
          }
        }, durationMs);
      };

      waterToggle.addEventListener('change', (e) => {
        if (e.target.checked) {
          if (!("Notification" in window)) {
            showToast("Tarayıcınız bildirimleri desteklemiyor.");
            e.target.checked = false;
            return;
          }
          if (Notification.permission !== "granted") {
            Notification.requestPermission().then(permission => {
              if (permission === "granted") {
                startWaterInterval(2 * 60 * 60 * 1000); // 2 hours
                showToast("Otomatik bildirimler açıldı! (2 Saatte Bir)");
              } else {
                e.target.checked = false;
                showToast("Bildirim izni reddedildi.");
              }
            });
          } else {
            startWaterInterval(2 * 60 * 60 * 1000); // 2 hours
            showToast("Otomatik bildirimler açıldı! (2 Saatte Bir)");
          }
        } else {
          if(waterIntervalId) clearInterval(waterIntervalId);
          showToast("Su bildirimleri kapatıldı.");
        }
      });
      
      document.getElementById('water-yes-btn').addEventListener('click', () => {
        document.getElementById('water-prompt-modal').classList.add('hidden');
        if (waterToggle.checked) startWaterInterval(2 * 60 * 60 * 1000); // Reset to 2 hours
        showToast("Harika! Süre 2 saat uzatıldı.");
      });
      
      document.getElementById('water-no-btn').addEventListener('click', () => {
        document.getElementById('water-prompt-modal').classList.add('hidden');
        if (waterToggle.checked) startWaterInterval(15 * 60 * 1000); // Remind in 15 mins
        showToast("Lütfen hemen bir bardak iç! 15 dk sonra tekrar soracağım.");
      });"""
content = content.replace(js_target, js_replacement)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Profile moved and water notification logic applied!")
