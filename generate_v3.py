import json

# Read the existing file to extract the foodDatabase
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract foodDatabase
start_idx = content.find('const foodDatabase = [')
end_idx = content.find('];', start_idx) + 2
if start_idx != -1 and end_idx != -1:
    food_db_str = content[start_idx:end_idx]
else:
    print("Could not find foodDatabase. Exiting.")
    exit(1)

new_html = f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Antigravity</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@500;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  
  <!-- Map -->
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin=""/>
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>
  
  <!-- html2canvas -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
  
  <style>
    :root {{
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
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; -webkit-tap-highlight-color: transparent; }}

    body {{
      background: radial-gradient(circle at top right, #112236 0%, var(--bg-color) 60%);
      color: var(--text-color);
      font-family: var(--font-body);
      line-height: 1.5;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }}

    h1, h2, h3 {{ font-family: var(--font-heading); font-weight: 700; }}

    .glass-card {{
      background: var(--surface-color);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid var(--surface-border);
      border-radius: 20px;
      padding: 20px;
      box-shadow: 0 8px 32px rgba(0,0,0,0.2);
      margin-bottom: 24px;
    }}

    header {{
      padding: 24px 20px 16px;
      text-align: center;
    }}

    header h1 {{
      font-size: 1.8rem;
      letter-spacing: -0.5px;
      color: var(--text-color);
      text-shadow: 0 0 10px var(--accent-glow);
    }}

    main {{
      flex: 1;
      padding: 10px 20px 100px;
      overflow-y: auto;
    }}

    .tab-content {{ display: none; animation: fadeSlideUp 0.4s ease forwards; }}
    .tab-content.active {{ display: block; }}

    @keyframes fadeSlideUp {{
      from {{ opacity: 0; transform: translateY(10px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    .section-title {{ font-size: 1.2rem; margin-bottom: 16px; display: flex; align-items: center; gap: 8px; }}
    .info-text {{ font-size: 0.875rem; color: var(--text-muted); }}

    /* Calorie Ring */
    .ring-container {{ position: relative; width: 220px; height: 220px; margin: 0 auto 24px; }}
    .ring-svg {{ width: 100%; height: 100%; transform: rotate(-90deg); }}
    .ring-bg {{ fill: none; stroke: var(--surface-border); stroke-width: 16; }}
    .ring-progress {{
      fill: none;
      stroke: var(--accent-color);
      stroke-width: 16;
      stroke-linecap: round;
      transition: stroke-dashoffset 1s cubic-bezier(0.4, 0, 0.2, 1);
      filter: drop-shadow(0 0 6px var(--accent-glow));
    }}
    .ring-inner {{
      position: absolute; top: 0; left: 0; width: 100%; height: 100%;
      display: flex; flex-direction: column; align-items: center; justify-content: center;
    }}
    .ring-inner .consumed {{ font-family: var(--font-heading); font-size: 3rem; font-weight: 700; line-height: 1; text-shadow: 0 0 10px rgba(255,255,255,0.2); }}
    .ring-inner .label {{ font-size: 0.875rem; color: var(--text-muted); margin-top: 4px; text-transform: uppercase; letter-spacing: 1px; }}

    .stats-row {{ display: flex; justify-content: space-between; text-align: center; margin-bottom: 24px; }}
    .stat-item .value {{ font-family: var(--font-heading); font-size: 1.4rem; font-weight: 700; }}
    .stat-item .label {{ font-size: 0.8rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.5px; }}

    /* Form Elements */
    .input-group {{ margin-bottom: 16px; }}
    label {{ display: block; font-size: 0.875rem; color: var(--text-muted); margin-bottom: 6px; }}
    input, select {{
      width: 100%;
      background: rgba(0,0,0,0.2);
      border: 1px solid var(--surface-border);
      color: var(--text-color);
      padding: 12px 16px;
      border-radius: 12px;
      font-family: var(--font-body);
      font-size: 1rem;
      transition: border-color 0.2s, box-shadow 0.2s;
    }}
    input:focus, select:focus {{ outline: none; border-color: var(--accent-color); box-shadow: 0 0 0 3px var(--accent-glow); }}
    
    button {{
      width: 100%;
      background: var(--accent-color);
      color: #000;
      border: none;
      padding: 14px;
      border-radius: 12px;
      font-family: var(--font-heading);
      font-weight: 700;
      font-size: 1rem;
      cursor: pointer;
      transition: transform 0.1s, box-shadow 0.2s;
      box-shadow: 0 4px 15px var(--accent-glow);
    }}
    button:active {{ transform: scale(0.98); }}
    button.secondary-btn {{ background: transparent; border: 1px solid var(--accent-color); color: var(--accent-color); box-shadow: none; }}
    button.danger-btn {{ background: var(--error-color); color: #fff; box-shadow: 0 4px 15px rgba(255,77,77,0.3); }}

    /* Lists */
    .meal-list {{ list-style: none; }}
    .meal-item {{
      display: flex; justify-content: space-between; align-items: center;
      padding: 12px 0; border-bottom: 1px solid var(--surface-border);
    }}
    .meal-item:last-child {{ border-bottom: none; }}
    .meal-name {{ font-weight: 500; font-size: 1rem; }}
    .meal-cal {{ font-family: var(--font-heading); color: var(--accent-color); font-weight: 700; }}
    .delete-btn {{
      background: transparent; border: none; color: var(--text-muted);
      width: 32px; height: 32px; border-radius: 50%; font-size: 1.2rem;
      padding: 0; box-shadow: none; display: flex; align-items: center; justify-content: center;
    }}

    .empty-state {{ text-align: center; color: var(--text-muted); font-size: 0.9rem; padding: 20px; }}

    /* Bottom Nav */
    nav {{
      position: fixed; bottom: 0; left: 0; width: 100%;
      background: rgba(11, 15, 25, 0.85);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-top: 1px solid var(--surface-border);
      display: flex; padding-bottom: env(safe-area-inset-bottom);
      z-index: 100;
    }}
    .nav-item {{
      flex: 1; display: flex; flex-direction: column; align-items: center;
      padding: 12px 0; background: none; border: none; box-shadow: none;
      color: var(--text-muted); gap: 4px; border-radius: 0;
    }}
    .nav-item svg {{ width: 24px; height: 24px; fill: currentColor; transition: transform 0.2s; }}
    .nav-item span {{ font-size: 0.7rem; font-weight: 500; }}
    .nav-item.active {{ color: var(--accent-color); }}
    .nav-item.active svg {{ transform: translateY(-2px); filter: drop-shadow(0 0 5px var(--accent-glow)); }}

    /* Map & Tracker */
    #walk-map {{ height: 250px; width: 100%; border-radius: 16px; margin-bottom: 20px; z-index: 1; border: 1px solid var(--surface-border); }}
    .activity-selector {{ display: flex; gap: 8px; margin-bottom: 16px; background: rgba(0,0,0,0.2); padding: 4px; border-radius: 12px; }}
    .act-btn {{
      flex: 1; background: transparent; color: var(--text-muted); box-shadow: none;
      padding: 8px; font-size: 0.875rem; border-radius: 8px; font-family: var(--font-body); font-weight: 500;
    }}
    .act-btn.active {{ background: var(--surface-color); color: var(--accent-color); border: 1px solid var(--surface-border); }}

    /* Overlays */
    .overlay {{
      position: fixed; top: 0; left: 0; width: 100%; height: 100%;
      background: var(--bg-color);
      z-index: 1000; display: flex; flex-direction: column; padding: 24px; overflow-y: auto;
    }}
    .overlay.hidden {{ display: none; }}
    .overlay-title {{ font-size: 2rem; color: var(--text-color); margin-bottom: 8px; text-shadow: 0 0 10px var(--accent-glow); }}

    /* Share Card */
    #share-card {{ background: var(--surface-color); border-radius: 20px; padding: 20px; text-align: center; border: 1px solid var(--accent-glow); }}
    #share-card h2 {{ font-size: 2.5rem; color: var(--accent-color); margin: 10px 0; }}
    #share-card .stats {{ display: flex; justify-content: space-around; margin-top: 20px; border-top: 1px solid var(--surface-border); padding-top: 16px; }}
    
    .toast {{
      position: fixed; bottom: 80px; left: 50%; transform: translateX(-50%) translateY(100px);
      background: var(--accent-color); color: #000; padding: 12px 24px; border-radius: 24px;
      font-weight: 600; font-size: 0.9rem; z-index: 2000; opacity: 0; transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: 0 4px 20px var(--accent-glow);
    }}
    .toast.show {{ transform: translateX(-50%) translateY(0); opacity: 1; }}

    .switch {{ position: relative; display: inline-block; width: 50px; height: 28px; }}
    .switch input {{ opacity: 0; width: 0; height: 0; }}
    .slider {{ position: absolute; cursor: pointer; top: 0; left: 0; right: 0; bottom: 0; background-color: rgba(255,255,255,0.1); transition: .4s; border-radius: 34px; }}
    .slider:before {{ position: absolute; content: ""; height: 20px; width: 20px; left: 4px; bottom: 4px; background-color: white; transition: .4s; border-radius: 50%; }}
    input:checked + .slider {{ background-color: var(--accent-color); box-shadow: 0 0 10px var(--accent-glow); }}
    input:checked + .slider:before {{ transform: translateX(22px); }}
    .toggle-container {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; }}
  </style>
</head>
<body>

  <header>
    <h1>Antigravity</h1>
    <p>Günlük Kalori ve Aktivite Asistanı</p>
  </header>

  <main>
    <!-- Tab 1: Bugün -->
    <section id="tab-home" class="tab-content active">
      <div class="glass-card">
        <div class="ring-container">
          <svg class="ring-svg" viewBox="0 0 224 224">
            <circle class="ring-bg" cx="112" cy="112" r="104"></circle>
            <circle class="ring-progress" id="calorie-ring" cx="112" cy="112" r="104"></circle>
          </svg>
          <div class="ring-inner">
            <div class="consumed" id="calories-consumed-main">0</div>
            <div class="label">Kcal Tüketildi</div>
          </div>
        </div>

        <div class="stats-row">
          <div class="stat-item">
            <div class="value" id="calories-goal">2000</div>
            <div class="label">Hedef</div>
          </div>
          <div class="stat-item">
            <div class="value" id="calories-burned" style="color: var(--accent-color)">0</div>
            <div class="label">Yakılan</div>
          </div>
          <div class="stat-item">
            <div class="value" id="calories-remaining">2000</div>
            <div class="label">Kalan</div>
          </div>
        </div>
        
        <p id="goal-exceeded-msg" class="info-text" style="color: var(--error-color); text-align: center; display: none;">
          Günlük hedefini aştın!
        </p>
      </div>

      <div class="glass-card">
        <form id="add-meal-form">
          <h2 class="section-title">Öğün Ekle</h2>
          <div class="input-group">
            <label for="meal-name">Yemek Ara veya Yaz</label>
            <input type="text" id="meal-name" list="food-db" placeholder="Örn: Yulaf ezmesi..." required autocomplete="off">
            <datalist id="food-db"></datalist>
          </div>
          <div style="display: flex; gap: 12px;">
            <div class="input-group" style="flex: 1.5;">
              <label for="meal-amount">Miktar / Birim</label>
              <div style="display: flex; gap: 8px;">
                <input type="number" id="meal-amount" placeholder="100" min="1" style="flex: 1;">
                <select id="meal-unit" style="flex: 1.5; padding: 0 4px; font-size: 0.8rem;">
                  <option value="1">Gram / ml</option>
                  <option value="200">Su Bardağı</option>
                  <option value="100">Çay Bardağı</option>
                  <option value="150">Porsiyon</option>
                </select>
              </div>
            </div>
            <div class="input-group" style="flex: 1;">
              <label for="meal-calories">Kalori (kcal)</label>
              <input type="number" id="meal-calories" placeholder="350" required min="1">
            </div>
          </div>
          <div class="info-text" id="meal-calc-info" style="margin-top: -8px; margin-bottom: 16px; display: none;">
            100 gramı <span id="unit-cal-display" style="color: var(--accent-color); font-weight: 600;">0</span> kcal.
          </div>
          <button type="submit">Öğün Ekle</button>
        </form>
      </div>

      <div class="glass-card">
        <h2 class="section-title">Bugün Tüketilenler</h2>
        <div id="empty-meals" class="empty-state">Henüz öğün eklemedin.</div>
        <ul id="meal-list" class="meal-list"></ul>
      </div>
    </section>

    <!-- Tab 2: Yürüyüş / Egzersiz -->
    <section id="tab-walk" class="tab-content">
      <div class="glass-card">
        <h2 class="section-title">Canlı Egzersiz Takibi</h2>
        <p class="info-text" style="margin-bottom: 16px;">GPS ile mesafeni ve kalorilerini takip et.</p>
        
        <div class="activity-selector" id="activity-selector">
          <button class="act-btn active" data-act="walk" data-met="3.5">🚶 Yürüyüş</button>
          <button class="act-btn" data-act="run" data-met="8.0">🏃 Koşu</button>
          <button class="act-btn" data-act="bike" data-met="6.0">🚴 Bisiklet</button>
        </div>
        
        <div id="walk-map-container" style="display: none;">
          <div id="walk-map"></div>
          <div class="stats-row" style="margin-top: 16px;">
            <div class="stat-item">
              <div class="value" id="track-time">00:00</div>
              <div class="label">Süre</div>
            </div>
            <div class="stat-item">
              <div class="value" id="track-dist">0.00</div>
              <div class="label">Km</div>
            </div>
            <div class="stat-item">
              <div class="value" id="track-cal" style="color: var(--accent-color)">0</div>
              <div class="label">Kcal</div>
            </div>
          </div>
        </div>

        <button type="button" id="start-walk-btn">Başla (GPS)</button>
        <button type="button" id="stop-walk-btn" class="danger-btn" style="display: none; margin-top: 16px;">Egzersizi Bitir</button>
        
        <div id="empty-walks" class="empty-state" style="margin-top: 16px;">Yürüyüş kaydın yok.</div>
      </div>
    </section>

    <!-- Tab 3: Ayarlar / Profil -->
    <section id="tab-reminder" class="tab-content">
      <div class="glass-card">
        <h2 class="section-title">Profil ve Ayarlar</h2>
        
        <button type="button" id="edit-profile-btn" class="secondary-btn" style="margin-bottom: 24px;">Profili Düzenle</button>

        <div class="input-group">
          <label for="settings-goal">Manuel Kalori Hedefi</label>
          <input type="number" id="settings-goal" placeholder="2000" min="500">
        </div>
        <button type="button" id="save-settings-btn" class="secondary-btn" style="margin-bottom: 32px;">Hedefi Güncelle</button>

        <div class="toggle-container">
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
        </div>
      </div>
    </section>
  </main>

  <nav>
    <button class="nav-item active" data-tab="tab-home">
      <svg viewBox="0 0 24 24"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg>
      <span>Bugün</span>
    </button>
    <button class="nav-item" data-tab="tab-walk">
      <svg viewBox="0 0 24 24"><path d="M13.5 5.5c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zM9.8 8.9L7 23h2.1l1.8-8 2.1 2v6h2v-7.5l-2.1-2 .6-3C14.8 12 16.8 13 19 13v-2c-1.9 0-3.5-1-4.3-2.4l-1-1.6c-.4-.6-1-1-1.7-1-.3 0-.5.1-.8.1L6 8.3V13h2V9.6l1.8-.7"/></svg>
      <span>Egzersiz</span>
    </button>
    <button class="nav-item" data-tab="tab-reminder">
      <svg viewBox="0 0 24 24"><path d="M12 22c1.1 0 2-.9 2-2h-4c0 1.1.9 2 2 2zm6-6v-5c0-3.07-1.63-5.64-4.5-6.32V4c0-.83-.67-1.5-1.5-1.5s-1.5.67-1.5 1.5v.68C7.64 5.36 6 7.92 6 11v5l-2 2v1h16v-1l-2-2zm-2 1H8v-6c0-2.48 1.51-4.5 4-4.5s4 2.02 4 4.5v6z"/></svg>
      <span>Ayarlar</span>
    </button>
  </nav>

  <div id="toast" class="toast"></div>

  <!-- Onboarding Modal -->
  <div id="onboarding" class="overlay hidden">
    <h1 class="overlay-title">Kişisel Profil</h1>
    <p class="info-text" style="margin-bottom: 24px;">Metabolizmana özel hedefler belirleyelim.</p>
    
    <div class="glass-card">
      <form id="onboarding-form">
        <div class="input-group">
          <label for="ob-gender">Cinsiyet</label>
          <select id="ob-gender" required>
            <option value="male">Erkek</option>
            <option value="female">Kadın</option>
          </select>
        </div>
        <div class="input-group">
          <label for="ob-age">Yaş</label>
          <input type="number" id="ob-age" placeholder="Örn: 25" required min="10" max="120">
        </div>
        <div class="input-group">
          <label for="ob-weight">Kilo (kg)</label>
          <input type="number" id="ob-weight" placeholder="Örn: 70" required min="30" max="250">
        </div>
        <div class="input-group">
          <label for="ob-height">Boy (cm)</label>
          <input type="number" id="ob-height" placeholder="Örn: 175" required min="100" max="250">
        </div>
        <div class="input-group">
          <label for="ob-activity">Hareketlilik Seviyesi</label>
          <select id="ob-activity" required>
            <option value="1.2">Masa başı (Hareketsiz)</option>
            <option value="1.375">Az hareketli (Haftada 1-3 gün spor)</option>
            <option value="1.55" selected>Orta (Haftada 3-5 gün spor)</option>
            <option value="1.725">Çok hareketli (Haftada 6-7 gün spor)</option>
          </select>
        </div>
        <button type="submit" style="margin-top: 16px;">Kaydet ve Başla</button>
        <button type="button" id="ob-cancel-btn" class="secondary-btn" style="margin-top: 12px; display: none;">İptal</button>
      </form>
    </div>
  </div>

  <!-- Summary Modal -->
  <div id="summary-modal" class="overlay hidden" style="justify-content: center; align-items: center; background: rgba(0,0,0,0.85); backdrop-filter: blur(5px);">
    <div id="share-card-container" style="width: 100%; max-width: 400px;">
      <div id="share-card">
        <h3 id="summary-title" style="color: var(--text-muted);">Egzersiz Özeti</h3>
        <h2 id="summary-cal">0 kcal</h2>
        <div class="stats">
          <div class="stat-item">
            <div class="value" id="summary-dist">0.00</div>
            <div class="label">Km</div>
          </div>
          <div class="stat-item">
            <div class="value" id="summary-time">00:00</div>
            <div class="label">Süre</div>
          </div>
        </div>
        <!-- Minimap wrapper for SS -->
        <div id="ss-map-container" style="height: 150px; margin-top: 16px; border-radius: 12px; overflow: hidden; display: none;"></div>
      </div>
      
      <div style="margin-top: 24px; display: flex; gap: 12px;">
        <button type="button" id="share-btn" style="flex: 1;">📸 Paylaş</button>
        <button type="button" id="close-summary-btn" class="secondary-btn" style="flex: 1;">Kapat</button>
      </div>
    </div>
  </div>

  <script>
    {food_db_str}

    let state = {{
      profileSetup: false,
      gender: 'male',
      age: 25,
      height: 175,
      activityLevel: 1.55,
      targetCalories: 2000,
      consumedCalories: 0,
      burnedCalories: 0,
      meals: [],
      walks: [],
      lastDate: null,
      reminderTime: '18:30',
      reminderEnabled: false,
      userWeight: 70
    }};

    const RING_CIRCUMFERENCE = 2 * Math.PI * 104;

    const el = {{
      ring: document.getElementById('calorie-ring'),
      consumedMain: document.getElementById('calories-consumed-main'),
      goalDisplay: document.getElementById('calories-goal'),
      burnedDisplay: document.getElementById('calories-burned'),
      remainingDisplay: document.getElementById('calories-remaining'),
      goalExceededMsg: document.getElementById('goal-exceeded-msg'),
      
      addMealForm: document.getElementById('add-meal-form'),
      mealNameInput: document.getElementById('meal-name'),
      mealAmountInput: document.getElementById('meal-amount'),
      mealUnitSelect: document.getElementById('meal-unit'),
      mealCaloriesInput: document.getElementById('meal-calories'),
      foodDbList: document.getElementById('food-db'),
      mealCalcInfo: document.getElementById('meal-calc-info'),
      unitCalDisplay: document.getElementById('unit-cal-display'),
      mealList: document.getElementById('meal-list'),
      emptyMeals: document.getElementById('empty-meals'),
      
      walkMapContainer: document.getElementById('walk-map-container'),
      startWalkBtn: document.getElementById('start-walk-btn'),
      stopWalkBtn: document.getElementById('stop-walk-btn'),
      trackTime: document.getElementById('track-time'),
      trackDist: document.getElementById('track-dist'),
      trackCal: document.getElementById('track-cal'),
      emptyWalks: document.getElementById('empty-walks'),
      
      settingsGoalInput: document.getElementById('settings-goal'),
      saveSettingsBtn: document.getElementById('save-settings-btn'),
      editProfileBtn: document.getElementById('edit-profile-btn'),
      
      reminderToggle: document.getElementById('reminder-toggle'),
      reminderSettings: document.getElementById('reminder-settings'),
      reminderTimeInput: document.getElementById('reminder-time'),
      saveReminderBtn: document.getElementById('save-reminder-btn'),
      
      toast: document.getElementById('toast'),
      navItems: document.querySelectorAll('.nav-item'),
      tabContents: document.querySelectorAll('.tab-content')
    }};

    el.ring.style.strokeDasharray = RING_CIRCUMFERENCE;

    // GPS Tracking variables
    let watchId = null;
    let walkStartTime = null;
    let walkPoints = [];
    let walkMapObj = null;
    let walkPolyline = null;
    let totalDistanceKm = 0;
    let currentWalkCal = 0;
    let trackInterval = null;
    let currentActivityMet = 3.5;
    let currentActivityName = 'Yürüyüş';

    function init() {{
      populateFoodList();
      loadState();
      checkOnboarding();
      checkMidnightReset();
      updateUI();
      setupEventListeners();
    }}

    function checkOnboarding() {{
      if (!state.profileSetup) {{
        document.getElementById('onboarding').classList.remove('hidden');
        document.getElementById('ob-cancel-btn').style.display = 'none';
      }}
    }}

    document.getElementById('onboarding-form').addEventListener('submit', (e) => {{
      e.preventDefault();
      state.gender = document.getElementById('ob-gender').value;
      state.age = parseInt(document.getElementById('ob-age').value, 10);
      state.userWeight = parseFloat(document.getElementById('ob-weight').value);
      state.height = parseInt(document.getElementById('ob-height').value, 10);
      state.activityLevel = parseFloat(document.getElementById('ob-activity').value);
      
      let bmr = 10 * state.userWeight + 6.25 * state.height - 5 * state.age;
      if (state.gender === 'male') bmr += 5;
      else bmr -= 161;
      
      state.targetCalories = Math.round(bmr * state.activityLevel);
      state.profileSetup = true;
      el.settingsGoalInput.value = state.targetCalories;
      
      saveState();
      document.getElementById('onboarding').classList.add('hidden');
      showToast('Profil güncellendi!');
    }});

    document.getElementById('ob-cancel-btn').addEventListener('click', () => {{
      document.getElementById('onboarding').classList.add('hidden');
    }});

    function loadState() {{
      const saved = localStorage.getItem('antigravity_state');
      if (saved) state = {{ ...state, ...JSON.parse(saved) }};
      
      el.settingsGoalInput.value = state.targetCalories;
      el.reminderTimeInput.value = state.reminderTime;
      el.reminderToggle.checked = state.reminderEnabled;
      toggleReminderSettings(state.reminderEnabled);
    }}

    function populateFoodList() {{
      foodDatabase.sort((a, b) => a.name.localeCompare(b.name, 'tr'));
      el.foodDbList.innerHTML = foodDatabase.map(f => `<option value="${{f.name}}">`).join('');
    }}

    function saveState() {{
      localStorage.setItem('antigravity_state', JSON.stringify(state));
      updateUI();
    }}

    function checkMidnightReset() {{
      const today = new Date().toDateString();
      if (state.lastDate !== today) {{
        state.consumedCalories = 0;
        state.burnedCalories = 0;
        state.meals = [];
        state.walks = [];
        state.lastDate = today;
        saveState();
      }}
    }}

    function updateUI() {{
      const netTarget = state.targetCalories + state.burnedCalories;
      let remaining = netTarget - state.consumedCalories;
      
      el.consumedMain.textContent = state.consumedCalories;
      el.goalDisplay.textContent = state.targetCalories;
      el.burnedDisplay.textContent = state.burnedCalories;
      el.remainingDisplay.textContent = remaining < 0 ? 0 : remaining;
      
      el.goalExceededMsg.style.display = remaining < 0 ? 'block' : 'none';

      let percent = state.consumedCalories / netTarget;
      if (percent > 1) percent = 1;
      if (isNaN(percent) || netTarget === 0) percent = 0;
      
      const offset = RING_CIRCUMFERENCE - (percent * RING_CIRCUMFERENCE);
      el.ring.style.strokeDashoffset = offset;

      el.mealList.innerHTML = '';
      if (state.meals.length === 0) {{
        el.emptyMeals.style.display = 'block';
      }} else {{
        el.emptyMeals.style.display = 'none';
        state.meals.forEach(meal => {{
          const li = document.createElement('li');
          li.className = 'meal-item';
          li.innerHTML = `
            <div class="meal-info">
              <div class="meal-name">${{escapeHTML(meal.name)}}</div>
              <div class="meal-cal">${{meal.calories}} kcal</div>
            </div>
            <button class="delete-btn" onclick="deleteMeal('${{meal.id}}')">&times;</button>
          `;
          el.mealList.appendChild(li);
        }});
      }}

      el.emptyWalks.style.display = (state.walks && state.walks.length > 0) ? 'none' : 'block';
    }}

    function setupEventListeners() {{
      el.navItems.forEach(item => {{
        item.addEventListener('click', (e) => {{
          e.preventDefault();
          const targetTabId = item.getAttribute('data-tab');
          el.navItems.forEach(nav => nav.classList.remove('active'));
          item.classList.add('active');
          el.tabContents.forEach(tab => tab.classList.remove('active'));
          document.getElementById(targetTabId).classList.add('active');
        }});
      }});

      const calculateMealCals = () => {{
        const name = el.mealNameInput.value.trim();
        const amount = parseFloat(el.mealAmountInput.value);
        const unitMultiplier = parseFloat(el.mealUnitSelect.value);
        const food = foodDatabase.find(f => f.name === name);
        
        if (food) {{
          el.mealCalcInfo.style.display = 'block';
          el.unitCalDisplay.textContent = food.cal;
          if (amount > 0) {{
            const totalWeight = amount * unitMultiplier;
            el.mealCaloriesInput.value = Math.round((food.cal * totalWeight) / 100);
          }}
        }} else {{
          el.mealCalcInfo.style.display = 'none';
        }}
      }};

      el.mealNameInput.addEventListener('input', calculateMealCals);
      el.mealAmountInput.addEventListener('input', calculateMealCals);
      el.mealUnitSelect.addEventListener('change', calculateMealCals);

      el.addMealForm.addEventListener('submit', (e) => {{
        e.preventDefault();
        let name = el.mealNameInput.value.trim();
        const amount = el.mealAmountInput.value.trim();
        const cal = parseInt(el.mealCaloriesInput.value, 10);
        
        if (name && cal > 0) {{
          if (amount) {{
            const unitMultiplier = parseFloat(el.mealUnitSelect.value);
            const unitText = el.mealUnitSelect.options[el.mealUnitSelect.selectedIndex].text;
            const unitSuffix = unitMultiplier === 1 ? 'g' : ` ${{unitText}}`;
            name += ` (${{amount}}${{unitSuffix}})`;
          }}
          state.meals.unshift({{
            id: Date.now().toString(), name, calories: cal, time: new Date().toISOString()
          }});
          state.consumedCalories += cal;
          
          pulseRing();
          el.mealNameInput.value = ''; el.mealAmountInput.value = ''; el.mealCaloriesInput.value = '';
          el.mealCalcInfo.style.display = 'none';
          saveState();
          showToast('Öğün eklendi');
        }}
      }});

      // Edit Profile
      el.editProfileBtn.addEventListener('click', () => {{
        document.getElementById('ob-gender').value = state.gender;
        document.getElementById('ob-age').value = state.age;
        document.getElementById('ob-weight').value = state.userWeight;
        document.getElementById('ob-height').value = state.height;
        document.getElementById('ob-activity').value = state.activityLevel;
        document.getElementById('onboarding').classList.remove('hidden');
        document.getElementById('ob-cancel-btn').style.display = 'block';
      }});

      // Activity Selector
      const actBtns = document.querySelectorAll('.act-btn');
      actBtns.forEach(btn => {{
        btn.addEventListener('click', () => {{
          actBtns.forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          currentActivityMet = parseFloat(btn.getAttribute('data-met'));
          currentActivityName = btn.innerText;
        }});
      }});

      // Walk map logic
      el.startWalkBtn.addEventListener('click', () => {{
        if (!("geolocation" in navigator)) {{
          showToast("Tarayıcınız GPS desteklemiyor.");
          return;
        }}
        
        el.walkMapContainer.style.display = 'block';
        el.startWalkBtn.style.display = 'none';
        el.stopWalkBtn.style.display = 'block';
        
        if (!walkMapObj) {{
          walkMapObj = L.map('walk-map').setView([41.0082, 28.9784], 15);
          L.tileLayer('https://{{s}}.basemaps.cartocdn.com/dark_all/{{z}}/{{x}}/{{y}}{{r}}.png', {{
            attribution: '© OpenStreetMap, © CartoDB'
          }}).addTo(walkMapObj);
          walkPolyline = L.polyline([], {{color: 'var(--accent-color)', weight: 5}}).addTo(walkMapObj);
        }}
        setTimeout(() => walkMapObj.invalidateSize(), 100);

        walkPoints = [];
        totalDistanceKm = 0;
        currentWalkCal = 0;
        walkStartTime = new Date();
        walkPolyline.setLatLngs([]);
        
        el.trackTime.textContent = "00:00";
        el.trackDist.textContent = "0.00";
        el.trackCal.textContent = "0";

        trackInterval = setInterval(() => {{
          if (!walkStartTime) return;
          const diffSecs = Math.floor((new Date() - walkStartTime) / 1000);
          const mins = Math.floor(diffSecs / 60);
          const secs = diffSecs % 60;
          el.trackTime.textContent = `${{String(mins).padStart(2, '0')}}:${{String(secs).padStart(2, '0')}}`;
          
          const diffHours = diffSecs / 3600;
          
          // Use selected activity MET, but if moving faster adjust dynamically for walking
          let met = currentActivityMet;
          const speedKmh = diffHours > 0 ? (totalDistanceKm / diffHours) : 0;
          if (currentActivityMet === 3.5 && speedKmh > 6) met = 4.3; // brisk walk
          
          currentWalkCal = Math.round(met * state.userWeight * diffHours);
          el.trackCal.textContent = currentWalkCal;
        }}, 1000);

        watchId = navigator.geolocation.watchPosition(
          (position) => {{
            const lat = position.coords.latitude;
            const lng = position.coords.longitude;
            const newPoint = L.latLng(lat, lng);
            
            if (walkPoints.length > 0) {{
              const lastPoint = walkPoints[walkPoints.length - 1];
              totalDistanceKm += (lastPoint.distanceTo(newPoint) / 1000);
            }}
            
            walkPoints.push(newPoint);
            walkPolyline.addLatLng(newPoint);
            walkMapObj.panTo(newPoint);
            el.trackDist.textContent = totalDistanceKm.toFixed(2);
          }},
          (err) => {{ console.error(err); }},
          {{ enableHighAccuracy: true, maximumAge: 10000, timeout: 5000 }}
        );
      }});

      el.stopWalkBtn.addEventListener('click', () => {{
        if (watchId) navigator.geolocation.clearWatch(watchId);
        clearInterval(trackInterval);
        
        el.startWalkBtn.style.display = 'block';
        el.stopWalkBtn.style.display = 'none';
        el.walkMapContainer.style.display = 'none';
        
        if (currentWalkCal > 0) {{
          state.burnedCalories += currentWalkCal;
          state.walks = state.walks || [];
          state.walks.push({{
            id: Date.now().toString(),
            type: currentActivityName,
            calories: currentWalkCal,
            distance: totalDistanceKm.toFixed(2),
            time: new Date().toISOString()
          }});
          
          pulseRing();
          saveState();
          showToast('Egzersiz bitti 💪');
          
          // Show summary modal
          document.getElementById('summary-title').textContent = currentActivityName + " Özeti";
          document.getElementById('summary-cal').textContent = currentWalkCal + " kcal";
          document.getElementById('summary-dist').textContent = totalDistanceKm.toFixed(2);
          document.getElementById('summary-time').textContent = el.trackTime.textContent;
          
          document.getElementById('summary-modal').classList.remove('hidden');
        }}
      }});

      // Close Summary
      document.getElementById('close-summary-btn').addEventListener('click', () => {{
        document.getElementById('summary-modal').classList.add('hidden');
      }});

      // Share SS
      document.getElementById('share-btn').addEventListener('click', async () => {{
        const btn = document.getElementById('share-btn');
        const origText = btn.innerHTML;
        btn.innerHTML = "Hazırlanıyor...";
        
        try {{
          const canvas = await html2canvas(document.getElementById('share-card'), {{
            backgroundColor: '#0b0f19',
            scale: 2,
            logging: false
          }});
          
          canvas.toBlob(async (blob) => {{
            const file = new File([blob], 'antigravity-workout.png', {{ type: 'image/png' }});
            if (navigator.canShare && navigator.canShare({{ files: [file] }})) {{
              await navigator.share({{
                title: 'Antigravity Egzersizim',
                text: 'Bugünkü egzersizimde yaktığım kalori! 💪 #Antigravity',
                files: [file]
              }});
            }} else {{
              // Fallback: download
              const url = URL.createObjectURL(blob);
              const a = document.createElement('a');
              a.href = url;
              a.download = 'antigravity-workout.png';
              a.click();
              URL.revokeObjectURL(url);
              showToast("Görüntü indirildi!");
            }}
            btn.innerHTML = origText;
          }}, 'image/png');
        }} catch(e) {{
          console.error(e);
          showToast("Paylaşım hazırlanırken hata oluştu.");
          btn.innerHTML = origText;
        }}
      }});

      // Settings
      el.saveSettingsBtn.addEventListener('click', () => {{
        const target = parseInt(el.settingsGoalInput.value, 10);
        if (target >= 500) {{
          state.targetCalories = target;
          saveState();
          showToast('Hedef güncellendi');
        }}
      }});

      // Reminders
      el.reminderToggle.addEventListener('change', (e) => {{
        const isEnabled = e.target.checked;
        state.reminderEnabled = isEnabled;
        toggleReminderSettings(isEnabled);
      }});

      el.saveReminderBtn.addEventListener('click', () => {{
        state.reminderTime = el.reminderTimeInput.value;
        saveState();
        showToast('Hatırlatıcı kaydedildi');
      }});
    }}

    function deleteMeal(id) {{
      const idx = state.meals.findIndex(m => m.id === id);
      if (idx !== -1) {{
        state.consumedCalories -= state.meals[idx].calories;
        if(state.consumedCalories < 0) state.consumedCalories = 0;
        state.meals.splice(idx, 1);
        saveState();
      }}
    }}

    function toggleReminderSettings(show) {{
      el.reminderSettings.style.opacity = show ? '1' : '0.5';
      el.reminderSettings.style.pointerEvents = show ? 'auto' : 'none';
    }}

    function pulseRing() {{
      el.ring.style.transform = 'scale(1.05)';
      el.ring.style.filter = 'drop-shadow(0 0 12px var(--accent-color))';
      setTimeout(() => {{
        el.ring.style.transform = 'scale(1)';
        el.ring.style.filter = 'drop-shadow(0 0 6px var(--accent-glow))';
      }}, 300);
    }}

    function showToast(msg) {{
      el.toast.textContent = msg;
      el.toast.classList.add('show');
      setTimeout(() => el.toast.classList.remove('show'), 3000);
    }}

    function escapeHTML(str) {{
      const div = document.createElement('div');
      div.textContent = str;
      return div.innerHTML;
    }}

    window.addEventListener('DOMContentLoaded', init);
  </script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("V3 UI Updated Successfully.")
