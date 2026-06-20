import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# --- 1. CSS Theme Overhaul & Compact Lists ---

css_target = """:root {
      --bg-color: #0b0f19;
      --surface-color: rgba(26, 32, 53, 0.7);
      --surface-border: rgba(255, 255, 255, 0.05);
      --accent-color: #00F5C3;
      --accent-glow: rgba(0, 245, 195, 0.4);
      --text-color: #ffffff;
      --text-muted: #8b9bb4;
      --error-color: #FF4D4D;
      
      --font-heading: 'DM Sans', sans-serif;
      --font-body: 'Inter', sans-serif;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; -webkit-tap-highlight-color: transparent; }

    body {
      background: radial-gradient(circle at top right, #112236 0%, var(--bg-color) 60%);
      color: var(--text-color);"""

css_replacement = """:root {
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
    }

    * { box-sizing: border-box; margin: 0; padding: 0; -webkit-tap-highlight-color: transparent; }

    body {
      background: var(--gradient-bg);
      color: var(--text-color);
      transition: background 0.3s, color 0.3s;"""
content = content.replace(css_target, css_replacement)

# Replace existing ring-bg stroke color to variable
content = content.replace("stroke: var(--surface-border); stroke-width: 16;", "stroke: var(--ring-bg); stroke-width: 16;")

# Add CSS for dropdown, compact list, and toggle
extra_css = """
    /* Theme & Dropdown additions */
    .theme-toggle { position: absolute; right: 20px; top: 24px; background: none; border: none; font-size: 1.5rem; cursor: pointer; box-shadow: none; width: auto; padding: 0; }
    
    .custom-dropdown {
      position: absolute; width: 100%; background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 12px;
      max-height: 250px; overflow-y: auto; z-index: 2000; box-shadow: 0 8px 32px rgba(0,0,0,0.3); display: none; margin-top: 4px; left: 0;
    }
    .dropdown-group-title { font-size: 0.8rem; font-weight: 700; color: var(--accent-color); padding: 8px 12px; background: var(--surface-color); border-bottom: 1px solid var(--surface-border); }
    .dropdown-item { padding: 10px 12px; font-size: 0.95rem; cursor: pointer; border-bottom: 1px solid var(--surface-border); transition: background 0.2s; }
    .dropdown-item:last-child { border-bottom: none; }
    .dropdown-item:hover { background: var(--surface-border); }

    .meal-list { list-style: none; max-height: 180px; overflow-y: auto; padding-right: 4px; }
    .meal-list::-webkit-scrollbar { width: 4px; }
    .meal-list::-webkit-scrollbar-thumb { background: var(--surface-border); border-radius: 4px; }
"""
content = content.replace("</style>", extra_css + "</style>")

# Set default theme
content = content.replace('<body>', '<body data-theme="light">')

# Add Theme Toggle Button
header_target = """  <header>
    <h1>Antigravity</h1>
    <p>Günlük Kalori ve Aktivite Asistanı</p>
  </header>"""
header_replacement = """  <header style="position: relative;">
    <h1>Antigravity</h1>
    <p>Günlük Kalori ve Aktivite Asistanı</p>
    <button id="theme-toggle-btn" class="theme-toggle">☀️</button>
  </header>"""
content = content.replace(header_target, header_replacement)

# --- 2. Custom Dropdown HTML ---
meal_input_target = """        <div class="input-group">
          <label for="meal-name">Yemek Ara veya Yaz</label>
          <input type="text" id="meal-name" list="food-db" placeholder="Örn: Yulaf ezmesi..." required autocomplete="off">
          <datalist id="food-db"></datalist>
        </div>"""
meal_input_replacement = """        <div class="input-group" style="position: relative;">
          <label for="meal-name">Yemek Ara veya Yaz</label>
          <input type="text" id="meal-name" placeholder="Örn: Yulaf ezmesi..." required autocomplete="off">
          <div id="custom-dropdown" class="custom-dropdown"></div>
        </div>"""
content = content.replace(meal_input_target, meal_input_replacement)

# --- 3. Move Reminder Widget ---
reminder_html = """        <div class="glass-card" id="reminder-widget" style="margin-bottom: 16px; padding: 12px 16px;">
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

# Remove old reminder from tab-reminder
old_reminder_regex = r"<div class=\"toggle-container\">.*?</div>\s*</div>" # Just a chunk to replace, let's use exact string search
old_reminder_block = """        <div class="toggle-container">
          <div>
            <label style="margin: 0; color: var(--text-color); font-size: 1rem;">Hatırlatıcılar</label>
            <div class="info-text">Günlük bildirim al</div>
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
          <button type="button" id="save-reminder-btn" class="secondary-btn">Saati Kaydet</button>
        </div>"""
content = content.replace(old_reminder_block, "")

# Insert reminder_html into tab-home, right before the first meal-category-card
insert_idx = content.find('<div class="glass-card meal-category-card">')
content = content[:insert_idx] + reminder_html + "\n\n      " + content[insert_idx:]


# --- 4. Expand Food DB with Types ---
start_idx = content.find('const foodDatabase = [')
end_idx = content.find('];', start_idx) + 2

new_food_db = """
    const foodDatabase = [
      // Kahvaltılıklar & Süt Ürünleri
      { name: "Yumurta (Haşlanmış)", cal: 155, adet: 50, porsiyon: 100, type: "Kahvaltılık & Süt" }, 
      { name: "Yumurta (Sahanda)", cal: 210, adet: 50, porsiyon: 100, type: "Kahvaltılık & Süt" }, 
      { name: "Omlet (Sade)", cal: 154, porsiyon: 120, type: "Kahvaltılık & Süt" },
      { name: "Menemen", cal: 170, porsiyon: 200, type: "Kahvaltılık & Süt" }, 
      { name: "Beyaz Peynir (Tam Yağlı)", cal: 310, porsiyon: 60, adet: 30, dilim: 30, type: "Kahvaltılık & Süt" }, 
      { name: "Beyaz Peynir (Light)", cal: 180, porsiyon: 60, adet: 30, dilim: 30, type: "Kahvaltılık & Süt" },
      { name: "Kaşar Peyniri", cal: 350, porsiyon: 40, adet: 20, dilim: 20, type: "Kahvaltılık & Süt" }, 
      { name: "Lor Peyniri", cal: 90, porsiyon: 50, type: "Kahvaltılık & Süt" }, 
      { name: "Tulum Peyniri", cal: 370, porsiyon: 40, adet: 20, dilim: 20, type: "Kahvaltılık & Süt" },
      { name: "Siyah Zeytin", cal: 105, adet: 4, porsiyon: 40, type: "Kahvaltılık & Süt" }, 
      { name: "Yeşil Zeytin", cal: 145, adet: 4, porsiyon: 40, type: "Kahvaltılık & Süt" }, 
      { name: "Tereyağı", cal: 717, adet: 10, porsiyon: 15, type: "Kahvaltılık & Süt" }, 
      { name: "Bal", cal: 304, adet: 15, porsiyon: 30, type: "Kahvaltılık & Süt" }, 
      { name: "Reçel", cal: 278, adet: 15, porsiyon: 30, type: "Kahvaltılık & Süt" }, 
      { name: "Tahin", cal: 595, adet: 15, porsiyon: 30, type: "Kahvaltılık & Süt" }, 
      { name: "Pekmez", cal: 290, adet: 15, porsiyon: 30, type: "Kahvaltılık & Süt" },
      { name: "Ekmek (Beyaz)", cal: 265, adet: 30, porsiyon: 60, dilim: 30, type: "Fırın Ürünleri" }, 
      { name: "Ekmek (Tam Buğday)", cal: 247, adet: 30, porsiyon: 60, dilim: 30, type: "Fırın Ürünleri" }, 
      { name: "Ekmek (Çavdar)", cal: 259, adet: 30, porsiyon: 60, dilim: 30, type: "Fırın Ürünleri" },
      { name: "Yulaf Ezmesi", cal: 389, adet: 10, porsiyon: 40, type: "Kahvaltılık & Süt" }, 
      { name: "Süt (Tam Yağlı)", cal: 61, porsiyon: 200, type: "Kahvaltılık & Süt" }, 
      { name: "Süt (Yarım Yağlı)", cal: 47, porsiyon: 200, type: "Kahvaltılık & Süt" },
      { name: "Süt (Laktozsuz)", cal: 43, porsiyon: 200, type: "Kahvaltılık & Süt" }, 
      { name: "Yoğurt (Tam Yağlı)", cal: 61, porsiyon: 200, type: "Kahvaltılık & Süt" }, 
      { name: "Süzme Yoğurt", cal: 112, porsiyon: 150, type: "Kahvaltılık & Süt" },
      { name: "Meyveli Yoğurt", cal: 95, porsiyon: 150, type: "Kahvaltılık & Süt" },
      { name: "Kefir", cal: 50, porsiyon: 200, type: "Kahvaltılık & Süt" }, 
      { name: "Sucuk", cal: 330, adet: 8, porsiyon: 50, dilim: 8, type: "Kahvaltılık & Süt" }, 
      { name: "Sosis", cal: 300, adet: 30, porsiyon: 90, type: "Kahvaltılık & Süt" }, 
      { name: "Pastırma", cal: 250, adet: 10, porsiyon: 50, dilim: 10, type: "Kahvaltılık & Süt" },
      { name: "Simit", cal: 275, adet: 100, porsiyon: 100, type: "Fırın Ürünleri" }, 
      { name: "Açma", cal: 350, adet: 120, porsiyon: 120, type: "Fırın Ürünleri" }, 
      { name: "Poğaça (Sade)", cal: 340, adet: 90, porsiyon: 90, type: "Fırın Ürünleri" },
      { name: "Poğaça (Peynirli)", cal: 330, adet: 90, porsiyon: 90, type: "Fırın Ürünleri" },
      { name: "Poğaça (Zeytinli)", cal: 350, adet: 90, porsiyon: 90, type: "Fırın Ürünleri" },
      { name: "Poğaça (Sosisli)", cal: 365, adet: 90, porsiyon: 90, type: "Fırın Ürünleri" },
      { name: "Poğaça (Kaşarlı)", cal: 360, adet: 90, porsiyon: 90, type: "Fırın Ürünleri" },
      { name: "Poğaça (Patatesli)", cal: 320, adet: 90, porsiyon: 90, type: "Fırın Ürünleri" },
      
      // Sebzeler & Meyveler
      { name: "Domates", cal: 18, adet: 110, porsiyon: 150, type: "Sebze & Meyve" }, 
      { name: "Salatalık", cal: 15, adet: 120, porsiyon: 150, type: "Sebze & Meyve" }, 
      { name: "Biber (Yeşil)", cal: 20, adet: 15, porsiyon: 100, type: "Sebze & Meyve" },
      { name: "Soğan", cal: 40, adet: 100, porsiyon: 100, type: "Sebze & Meyve" }, 
      { name: "Patates (Haşlama)", cal: 87, adet: 150, porsiyon: 200, type: "Sebze & Meyve" }, 
      { name: "Patates Kızartması", cal: 312, porsiyon: 150, type: "Sebze & Meyve" },
      { name: "Havuç", cal: 41, adet: 80, porsiyon: 100, type: "Sebze & Meyve" }, 
      { name: "Kabak", cal: 16, adet: 150, porsiyon: 200, type: "Sebze & Meyve" }, 
      { name: "Patlıcan", cal: 25, adet: 200, porsiyon: 200, type: "Sebze & Meyve" }, 
      { name: "Brokoli", cal: 34, porsiyon: 150, type: "Sebze & Meyve" },
      { name: "Karnabahar", cal: 25, porsiyon: 150, type: "Sebze & Meyve" }, 
      { name: "Mantar", cal: 22, adet: 15, porsiyon: 150, type: "Sebze & Meyve" }, 
      { name: "Elma", cal: 52, adet: 150, porsiyon: 150, type: "Sebze & Meyve" }, 
      { name: "Muz", cal: 89, adet: 120, porsiyon: 120, type: "Sebze & Meyve" },
      { name: "Portakal", cal: 47, adet: 130, porsiyon: 130, type: "Sebze & Meyve" }, 
      { name: "Mandalina", cal: 53, adet: 80, porsiyon: 160, type: "Sebze & Meyve" }, 
      { name: "Çilek", cal: 32, adet: 12, porsiyon: 150, type: "Sebze & Meyve" }, 
      { name: "Karpuz", cal: 30, dilim: 200, porsiyon: 200, type: "Sebze & Meyve" }, 
      { name: "Kavun", cal: 34, dilim: 200, porsiyon: 200, type: "Sebze & Meyve" }, 
      { name: "Üzüm", cal: 69, porsiyon: 150, type: "Sebze & Meyve" }, 
      { name: "Kiraz", cal: 50, adet: 6, porsiyon: 150, type: "Sebze & Meyve" }, 
      { name: "Şeftali", cal: 39, adet: 150, porsiyon: 150, type: "Sebze & Meyve" },
      
      // Çorbalar
      { name: "Mercimek Çorbası", cal: 56, porsiyon: 250, type: "Çorbalar" }, 
      { name: "Ezogelin Çorbası", cal: 54, porsiyon: 250, type: "Çorbalar" },
      { name: "Tarhana Çorbası", cal: 60, porsiyon: 250, type: "Çorbalar" }, 
      { name: "Tavuk Suyu Çorbası", cal: 45, porsiyon: 250, type: "Çorbalar" }, 
      { name: "Domates Çorbası", cal: 35, porsiyon: 250, type: "Çorbalar" }, 
      { name: "Yayla Çorbası", cal: 40, porsiyon: 250, type: "Çorbalar" }, 
      { name: "Kelle Paça", cal: 135, porsiyon: 250, type: "Çorbalar" }, 

      // Ana Yemekler
      { name: "Pirinç Pilavı", cal: 130, porsiyon: 150, type: "Ana Yemekler" }, 
      { name: "Bulgur Pilavı", cal: 83, porsiyon: 150, type: "Ana Yemekler" }, 
      { name: "Makarna (Sade, Pişmiş)", cal: 158, porsiyon: 150, type: "Ana Yemekler" },
      { name: "Tavuk Göğsü (Izgara)", cal: 165, adet: 150, porsiyon: 150, type: "Ana Yemekler" }, 
      { name: "Tavuk But (Fırın)", cal: 210, adet: 120, porsiyon: 200, type: "Ana Yemekler" }, 
      { name: "Dana Eti (Az Yağlı)", cal: 250, porsiyon: 150, type: "Ana Yemekler" },
      { name: "Köfte (Izgara)", cal: 200, adet: 30, porsiyon: 120, type: "Ana Yemekler" }, 
      { name: "Kıyma (Dana)", cal: 332, porsiyon: 100, type: "Ana Yemekler" }, 
      { name: "Somon Balığı", cal: 208, porsiyon: 200, type: "Ana Yemekler" },
      { name: "Ton Balığı (Süzülmüş)", cal: 116, adet: 160, porsiyon: 160, type: "Ana Yemekler" }, 
      { name: "Nohut Yemeği", cal: 164, porsiyon: 200, type: "Ana Yemekler" },
      { name: "Kuru Fasulye Yemeği", cal: 135, porsiyon: 200, type: "Ana Yemekler" }, 
      { name: "Zeytinyağlı Taze Fasulye", cal: 48, porsiyon: 200, type: "Ana Yemekler" }, 
      { name: "Ispanak Yemeği", cal: 45, porsiyon: 200, type: "Ana Yemekler" },
      { name: "Karnıyarık", cal: 130, adet: 200, porsiyon: 200, type: "Ana Yemekler" }, 
      { name: "Mantı", cal: 170, porsiyon: 200, type: "Ana Yemekler" }, 
      { name: "Lahmacun", cal: 200, adet: 150, porsiyon: 150, type: "Ana Yemekler" }, 
      { name: "Pide (Kıymalı)", cal: 240, porsiyon: 200, type: "Ana Yemekler" }, 
      { name: "Döner (Et)", cal: 250, porsiyon: 150, type: "Ana Yemekler" }, 
      { name: "Döner (Tavuk)", cal: 195, porsiyon: 150, type: "Ana Yemekler" },
      { name: "İskender Kebap", cal: 200, porsiyon: 400, type: "Ana Yemekler" }, 
      { name: "Adana Kebap", cal: 230, adet: 150, porsiyon: 150, type: "Ana Yemekler" }, 
      { name: "Tavuk Şiş", cal: 160, adet: 100, porsiyon: 200, type: "Ana Yemekler" }, 

      // Pizzalar
      { name: "Pizza (Küçük Boy)", cal: 260, dilim: 70, adet: 420, porsiyon: 210, type: "Pizza" }, 
      { name: "Pizza (Orta Boy)", cal: 260, dilim: 100, adet: 800, porsiyon: 300, type: "Pizza" }, 
      { name: "Pizza (Büyük Boy)", cal: 260, dilim: 130, adet: 1040, porsiyon: 390, type: "Pizza" }, 
      { name: "Pizza (İnce Hamur İtalyan)", cal: 220, dilim: 80, porsiyon: 240, type: "Pizza" },
      
      // Mezeler & Salatalar
      { name: "Cacık", cal: 45, porsiyon: 200, type: "Meze & Salata" },
      { name: "Haydari", cal: 110, porsiyon: 150, type: "Meze & Salata" },
      { name: "Şakşuka", cal: 130, porsiyon: 150, type: "Meze & Salata" },
      { name: "Çoban Salata", cal: 30, porsiyon: 200, type: "Meze & Salata" },
      { name: "Mevsim Salata", cal: 25, porsiyon: 200, type: "Meze & Salata" },
      { name: "Rus Salatası", cal: 220, porsiyon: 150, type: "Meze & Salata" },
      { name: "Humus", cal: 160, porsiyon: 150, type: "Meze & Salata" },
      { name: "Kısır", cal: 180, porsiyon: 150, type: "Meze & Salata" },
      { name: "Çiğ Köfte (Etsiz)", cal: 180, adet: 25, porsiyon: 150, type: "Meze & Salata" },
      
      // Atıştırmalıklar & Kuruyemiş & Tatlı
      { name: "Ceviz", cal: 654, adet: 5, porsiyon: 30, type: "Atıştırmalık & Tatlı" }, 
      { name: "Badem", cal: 579, adet: 1.5, porsiyon: 30, type: "Atıştırmalık & Tatlı" }, 
      { name: "Fındık", cal: 628, adet: 1.5, porsiyon: 30, type: "Atıştırmalık & Tatlı" }, 
      { name: "Fıstık (Kavrulmuş)", cal: 585, adet: 1, porsiyon: 30, type: "Atıştırmalık & Tatlı" },
      { name: "Leblebi (Sarı)", cal: 380, porsiyon: 30, type: "Atıştırmalık & Tatlı" }, 
      { name: "Leblebi (Beyaz)", cal: 360, porsiyon: 30, type: "Atıştırmalık & Tatlı" }, 
      { name: "Kaju", cal: 553, adet: 2, porsiyon: 30, type: "Atıştırmalık & Tatlı" },
      { name: "Antep Fıstığı", cal: 560, adet: 1, porsiyon: 30, type: "Atıştırmalık & Tatlı" }, 
      { name: "Zeytinyağı", cal: 884, adet: 10, porsiyon: 15, type: "Atıştırmalık & Tatlı" }, 
      { name: "Ayçiçek Yağı", cal: 884, adet: 10, porsiyon: 15, type: "Atıştırmalık & Tatlı" },
      { name: "Çikolata (Sütlü)", cal: 535, adet: 5, porsiyon: 40, type: "Atıştırmalık & Tatlı" }, 
      { name: "Çikolata (Bitter)", cal: 546, adet: 5, porsiyon: 40, type: "Atıştırmalık & Tatlı" }, 
      { name: "Bisküvi (Sade)", cal: 433, adet: 6, porsiyon: 30, type: "Atıştırmalık & Tatlı" },
      { name: "Kek (Sade)", cal: 365, adet: 60, dilim: 60, porsiyon: 100, type: "Atıştırmalık & Tatlı" }, 
      { name: "Dondurma", cal: 207, adet: 50, porsiyon: 100, type: "Atıştırmalık & Tatlı" }, 
      { name: "Baklava", cal: 420, adet: 40, dilim: 40, porsiyon: 120, type: "Atıştırmalık & Tatlı" }, 
      { name: "Sütlaç", cal: 110, porsiyon: 250, type: "Atıştırmalık & Tatlı" }, 
      { name: "Kazandibi", cal: 130, porsiyon: 200, type: "Atıştırmalık & Tatlı" }, 
      { name: "Profiterol", cal: 280, porsiyon: 200, type: "Atıştırmalık & Tatlı" },
      { name: "Cips (Patates)", cal: 536, porsiyon: 50, type: "Atıştırmalık & Tatlı" }, 
      { name: "Patlamış Mısır (Sade)", cal: 387, porsiyon: 50, type: "Atıştırmalık & Tatlı" }, 
      { name: "Kraker (Tuzlu)", cal: 500, porsiyon: 40, type: "Atıştırmalık & Tatlı" },
      { name: "Protein Bar", cal: 350, adet: 50, porsiyon: 50, type: "Atıştırmalık & Tatlı" }, 
      { name: "Granola", cal: 470, porsiyon: 50, type: "Atıştırmalık & Tatlı" }, 
      { name: "Müsli", cal: 350, porsiyon: 50, type: "Atıştırmalık & Tatlı" },
      
      // İçecekler
      { name: "Kola", cal: 42, adet: 330, porsiyon: 250, type: "İçecekler" }, 
      { name: "Kola (Şekersiz)", cal: 0, adet: 330, porsiyon: 250, type: "İçecekler" }, 
      { name: "Meyve Suyu", cal: 45, adet: 200, porsiyon: 200, type: "İçecekler" },
      { name: "Ayran", cal: 37, adet: 200, porsiyon: 200, type: "İçecekler" }, 
      { name: "Çay (Şekersiz)", cal: 0, porsiyon: 100, type: "İçecekler" }, 
      { name: "Filtre Kahve (Sade)", cal: 1, porsiyon: 250, type: "İçecekler" },
      { name: "Türk Kahvesi (Sade)", cal: 2, porsiyon: 70, type: "İçecekler" }, 
      { name: "Latte", cal: 45, porsiyon: 350, type: "İçecekler" }, 
      { name: "Mocha", cal: 80, porsiyon: 350, type: "İçecekler" },
      { name: "Limonata", cal: 40, porsiyon: 250, type: "İçecekler" }, 
      { name: "Bira", cal: 43, adet: 500, porsiyon: 500, type: "İçecekler" }, 
      { name: "Şarap (Kırmızı)", cal: 85, porsiyon: 150, type: "İçecekler" },
      { name: "Maden Suyu (Sade)", cal: 0, adet: 200, porsiyon: 200, type: "İçecekler" }, 
      { name: "Maden Suyu (Meyveli)", cal: 25, adet: 200, porsiyon: 200, type: "İçecekler" }, 
      { name: "Soğuk Çay (Ice Tea)", cal: 30, porsiyon: 250, type: "İçecekler" }
    ];
"""

content = content[:start_idx] + new_food_db + content[end_idx:]

# --- 5. Custom Dropdown JS and Theme Logic ---
el_replace_target = "foodDbList: document.getElementById('food-db'),"
el_replace = """customDropdown: document.getElementById('custom-dropdown'),
      themeToggleBtn: document.getElementById('theme-toggle-btn'),"""
content = content.replace(el_replace_target, el_replace)

setup_ev_target = """      document.querySelectorAll('.add-meal-btn').forEach(btn => {"""
setup_ev_replace = """      // Theme Toggle Logic
      let currentTheme = localStorage.getItem('antigravity_theme') || 'light';
      document.body.setAttribute('data-theme', currentTheme);
      el.themeToggleBtn.textContent = currentTheme === 'light' ? '🌙' : '☀️';

      el.themeToggleBtn.addEventListener('click', () => {
        currentTheme = currentTheme === 'light' ? 'dark' : 'light';
        document.body.setAttribute('data-theme', currentTheme);
        el.themeToggleBtn.textContent = currentTheme === 'light' ? '🌙' : '☀️';
        localStorage.setItem('antigravity_theme', currentTheme);
      });

      // Custom Dropdown Logic
      const renderDropdown = (query) => {
        el.customDropdown.innerHTML = '';
        if (!query) {
          el.customDropdown.style.display = 'none';
          return;
        }
        
        const q = query.toLowerCase();
        const results = foodDatabase.filter(f => f.name.toLowerCase().includes(q));
        
        if (results.length === 0) {
          el.customDropdown.style.display = 'none';
          return;
        }

        // Group by type
        const grouped = {};
        results.forEach(f => {
          if (!grouped[f.type]) grouped[f.type] = [];
          grouped[f.type].push(f);
        });

        Object.keys(grouped).forEach(type => {
          const title = document.createElement('div');
          title.className = 'dropdown-group-title';
          title.textContent = type;
          el.customDropdown.appendChild(title);
          
          grouped[type].forEach(f => {
            const item = document.createElement('div');
            item.className = 'dropdown-item';
            item.textContent = f.name;
            item.addEventListener('click', () => {
              el.mealNameInput.value = f.name;
              el.customDropdown.style.display = 'none';
              calculateMealCals();
            });
            el.customDropdown.appendChild(item);
          });
        });
        
        el.customDropdown.style.display = 'block';
      };

      el.mealNameInput.addEventListener('input', (e) => {
        renderDropdown(e.target.value);
        calculateMealCals();
      });

      document.addEventListener('click', (e) => {
        if (!el.customDropdown.contains(e.target) && e.target !== el.mealNameInput) {
          el.customDropdown.style.display = 'none';
        }
      });

      document.querySelectorAll('.add-meal-btn').forEach(btn => {"""
content = content.replace(setup_ev_target, setup_ev_replace)

# Remove the populateFoodList function since we use custom dropdown now
content = re.sub(r"function populateFoodList\(\) \{[\s\S]*?\}", "", content)
content = content.replace("populateFoodList();", "")

# Write to file
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("V5 generated successfully!")
