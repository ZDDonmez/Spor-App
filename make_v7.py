import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Extract head and foodDatabase
head_end = content.find('</head>')
head = content[:head_end+7]

style_start = content.find('<style>')
style_end = content.find('</style>')
style = content[style_start:style_end+8]

food_db_start = content.find('const foodDatabase = [')
food_db_end = content.find('];', food_db_start) + 2
food_db = content[food_db_start:food_db_end]

# Modify styles for the new layout
new_styles = """
    /* V7 Dashboard Additions */
    .dashboard-container { padding-bottom: 40px; }
    .meal-dash-btn { 
      background: var(--surface-color); border: 1px solid var(--surface-border); border-radius: 16px; 
      padding: 16px; color: var(--text-color); font-family: var(--font-heading); font-weight: 700; font-size: 1.1rem;
      text-transform: uppercase; letter-spacing: 1px; cursor: pointer; transition: all 0.2s;
      display: flex; justify-content: space-between; align-items: center; backdrop-filter: blur(24px);
    }
    .meal-dash-btn:hover { background: rgba(0, 169, 143, 0.1); border-color: var(--accent-color); }
    .meal-dash-cal { color: var(--accent-color); font-size: 0.9rem; font-weight: 700; }
    
    #map { transition: height 0.3s ease; }
    
    .manager-cal-total { font-size: 2rem; font-family: var(--font-heading); font-weight: 800; color: var(--accent-color); text-align: center; margin-bottom: 24px; }
"""
style = style.replace('</style>', new_styles + '</style>')

body_html = """
<body data-theme="light">
  <header style="position: relative; display: flex; align-items: center; justify-content: center; margin-bottom: 24px; min-height: 60px;">
    <button id="profile-modal-btn" class="theme-toggle" style="position: absolute; left: 0; color: var(--text-color);">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
    </button>
    <div style="text-align: center; z-index: 1;">
      <img src="metra_logo.png" alt="METRA Logo" style="width: 48px; height: 48px; border-radius: 12px; margin-bottom: 8px; box-shadow: 0 4px 12px rgba(0,169,143,0.3);">
      <h1 style="font-size: 1.5rem; letter-spacing: 3px; font-weight: 800; background: linear-gradient(90deg, var(--text-color), var(--accent-color)); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">METRA</h1>
    </div>
    <button id="theme-toggle-btn" class="theme-toggle" style="position: absolute; right: 0; color: var(--text-color);">
      <div id="theme-icon-container"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg></div>
    </button>
  </header>

  <main class="dashboard-container">
    <!-- Top Section: Ring + Meals -->
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
    </div>

    <!-- Middle Section: Exercise & GPS -->
    <div class="glass-card">
      <h2 class="section-title">Egzersiz & GPS</h2>
      <div class="input-group">
        <select id="activity-type" style="width: 100%; padding: 12px; border-radius: 8px; border: 1px solid var(--surface-border); background: var(--bg-color); color: var(--text-color); margin-bottom: 12px; font-family: var(--font-body);">
          <option value="walk">🏃‍♂️ Yürüyüş</option>
          <option value="run">🏃‍♀️ Koşu</option>
          <option value="bike">🚴 Bisiklet</option>
        </select>
      </div>
      
      <div id="map" style="width: 100%; height: 200px; background: var(--bg-color); border-radius: 12px; margin-bottom: 16px; display: none; z-index: 1;"></div>
      
      <div class="stats-row" id="live-walk-stats" style="display: none; margin-bottom: 16px;">
        <div class="stat-item">
          <div class="value" id="live-distance">0.00</div>
          <div class="label">Mesafe (km)</div>
        </div>
        <div class="stat-item">
          <div class="value" id="live-cal" style="color: var(--accent-color)">0</div>
          <div class="label">Yakılan</div>
        </div>
      </div>
      
      <button type="button" id="start-walk-btn">Başla (GPS)</button>
      <button type="button" id="stop-walk-btn" class="danger-btn" style="display: none; margin-top: 12px;">Egzersizi Bitir</button>
      <div id="empty-walks" class="empty-state" style="margin-top: 16px;">Yürüyüş kaydın yok.</div>
    </div>

    <!-- Bottom Section: Alarm & Calendar -->
    <div class="glass-card">
      <h2 class="section-title">Spor Hatırlatıcı Alarm</h2>
      <div class="info-text" style="margin-bottom: 16px;">Her gün antrenman veya su içme vakti geldiğinde telefonunun çalması için takvime ekle.</div>
      <div style="display: flex; gap: 12px; align-items: center;">
        <input type="time" id="reminder-time" value="18:30" style="flex: 1; padding: 12px; border-radius: 8px; border: 1px solid var(--surface-border); background: var(--bg-color); color: var(--text-color);">
        <button id="add-to-calendar-btn" class="primary-btn" style="flex: 2; margin: 0; display: flex; justify-content: center; align-items: center; gap: 8px;">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
          Takvime Ekle
        </button>
      </div>
    </div>
  </main>

  <!-- Meal Manager Modal -->
  <div id="meal-manager-modal" class="overlay hidden" style="justify-content: flex-end; padding: 0; background: rgba(0,0,0,0.6);">
    <div class="glass-card" style="margin-bottom: 0; border-radius: 24px 24px 0 0; padding-bottom: 40px; animation: fadeSlideUp 0.3s ease; max-height: 90vh; overflow-y: auto;">
      <div style="display: flex; justify-content: space-between; align-items: center;">
        <h2 class="section-title" id="manager-title" style="color: var(--accent-color); margin-bottom: 0;">Öğün</h2>
        <button type="button" id="close-manager-modal" style="background: none; border: none; color: var(--text-color); font-size: 1.5rem; cursor: pointer;">&times;</button>
      </div>
      <div id="manager-cal-total" class="manager-cal-total">0 kcal</div>
      
      <ul id="manager-list" class="meal-list" style="margin-bottom: 24px;"></ul>
      
      <form id="add-meal-form">
        <h3 style="margin-bottom: 12px; font-family: var(--font-heading); font-size: 1rem;">Yeni Yemek Ekle</h3>
        <div class="input-group" style="position: relative;">
          <label for="meal-name">Yemek Ara veya Yaz</label>
          <input type="text" id="meal-name" placeholder="Örn: Yulaf ezmesi..." required autocomplete="off">
          <div id="custom-dropdown" class="custom-dropdown"></div>
        </div>
        <div style="display: flex; gap: 12px;">
          <div class="input-group" style="flex: 1.5;">
            <label for="meal-amount">Miktar / Birim</label>
            <div style="display: flex; gap: 8px;">
              <input type="number" id="meal-amount" placeholder="Örn: 1 veya 0.5" min="0.1" step="0.1" style="flex: 1;">
              <select id="meal-unit" style="flex: 1.5; padding: 0 4px; font-size: 0.8rem;">
                <option value="1">Gram / ml</option>
                <option value="200">Su Bardağı</option>
                <option value="100">Çay Bardağı</option>
                <option value="150">Porsiyon</option>
                <option value="1">Adet</option>
                <option value="1">Dilim</option>
              </select>
            </div>
          </div>
          <div class="input-group" style="flex: 1;">
            <label for="meal-calories">Kalori (kcal)</label>
            <input type="number" id="meal-calories" placeholder="350" required min="1">
          </div>
        </div>
        <div class="info-text" id="meal-calc-info" style="margin-top: -8px; margin-bottom: 16px; display: none;">
          <span id="unit-cal-display" style="color: var(--accent-color); font-weight: 600;">0</span> kcal.
        </div>
        <button type="submit" style="margin-bottom: 12px;">Ekle</button>
      </form>
    </div>
  </div>

  <!-- Profile Settings Modal -->
  <div id="profile-modal" class="overlay hidden" style="background: rgba(0,0,0,0.6);">
    <div class="glass-card" style="width: 100%; max-width: 400px; animation: fadeSlideUp 0.3s ease;">
      <h2 class="section-title">Profili Düzenle</h2>
      <div class="input-group">
        <label for="settings-goal">Günlük Kalori Hedefi</label>
        <input type="number" id="settings-goal" placeholder="Örn: 2000" min="500">
      </div>
      <button type="button" id="save-settings-btn" style="margin-bottom: 12px;">Kaydet</button>
      <button type="button" id="close-profile-modal" class="secondary-btn">Kapat</button>
      <button type="button" id="clear-data-btn" class="danger-btn" style="margin-top: 24px;">Tüm Verileri Sil (Sıfırla)</button>
    </div>
  </div>

  <!-- Onboarding Modal (Preserved) -->
  <div id="onboarding" class="overlay hidden">
    <div class="glass-card" style="width: 100%; max-width: 400px; max-height: 90vh; overflow-y: auto;">
      <h2 class="section-title" style="color: var(--accent-color); font-size: 1.8rem; text-align: center;">Hoş Geldin!</h2>
      <p style="text-align: center; margin-bottom: 24px; color: var(--text-muted);">Seni daha iyi tanıyıp sana özel hedefler belirleyelim.</p>
      
      <form id="onboarding-form">
        <div class="input-group">
          <label>Cinsiyet</label>
          <select id="ob-gender" required>
            <option value="male">Erkek</option>
            <option value="female">Kadın</option>
          </select>
        </div>
        <div style="display: flex; gap: 12px;">
          <div class="input-group" style="flex: 1;">
            <label>Yaş</label>
            <input type="number" id="ob-age" min="10" max="100" required>
          </div>
          <div class="input-group" style="flex: 1;">
            <label>Boy (cm)</label>
            <input type="number" id="ob-height" min="100" max="250" required>
          </div>
          <div class="input-group" style="flex: 1;">
            <label>Kilo (kg)</label>
            <input type="number" id="ob-weight" min="30" max="300" required>
          </div>
        </div>
        <div class="input-group">
          <label>Hareket Seviyesi</label>
          <select id="ob-activity" required>
            <option value="1.2">Masa başı (Sedanter)</option>
            <option value="1.375">Hafif hareketli (Haftada 1-3 gün spor)</option>
            <option value="1.55">Orta hareketli (Haftada 3-5 gün spor)</option>
            <option value="1.725">Çok hareketli (Haftada 6-7 gün spor)</option>
            <option value="1.9">Aşırı hareketli (Ağır idman/sporcu)</option>
          </select>
        </div>
        <button type="submit" style="margin-top: 16px;">Profili Oluştur</button>
        <button type="button" id="ob-cancel-btn" class="secondary-btn" style="display: none; margin-top: 8px;">İptal</button>
      </form>
    </div>
  </div>

  <!-- Activity Summary Modal (Preserved) -->
  <div id="activity-summary-modal" class="overlay hidden" style="justify-content: center; align-items: center; padding: 20px;">
    <div class="glass-card" id="summary-card" style="width: 100%; max-width: 350px; text-align: center; border: 1px solid var(--accent-color);">
      <h2 class="section-title" id="summary-title" style="color: var(--accent-color);">Egzersiz Özeti</h2>
      <div style="font-size: 3rem; margin: 20px 0;">🏃‍♂️</div>
      <div style="display: flex; justify-content: space-around; margin-bottom: 24px;">
        <div>
          <div id="summary-distance" style="font-size: 1.5rem; font-weight: bold;">0.00</div>
          <div style="color: var(--text-muted); font-size: 0.9rem;">Mesafe (km)</div>
        </div>
        <div>
          <div id="summary-cal" style="font-size: 1.5rem; font-weight: bold; color: var(--accent-color);">0</div>
          <div style="color: var(--text-muted); font-size: 0.9rem;">Yakılan (kcal)</div>
        </div>
      </div>
      <button type="button" id="share-summary-btn" style="margin-bottom: 12px; background: #fff; color: #000;">📸 Resmi Paylaş</button>
      <button type="button" id="close-summary-btn" class="secondary-btn">Kapat</button>
    </div>
  </div>

  <div id="toast" class="toast">Kaydedildi!</div>

  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
  <script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script>
  <script>
    PLACEHOLDER_DB

    let state = {
      profileSetup: false, gender: 'male', age: 25, height: 175, activityLevel: 1.55,
      targetCalories: 2000, consumedCalories: 0, burnedCalories: 0, meals: [], walks: [],
      lastDate: null, userWeight: 70
    };

    const RING_CIRCUMFERENCE = 2 * Math.PI * 104;

    const el = {
      ring: document.getElementById('calorie-ring'),
      ringBurned: document.getElementById('calorie-ring-burned'),
      consumedMain: document.getElementById('calories-consumed-main'),
      goalDisplay: document.getElementById('calories-goal'),
      goalExceededMsg: document.getElementById('goal-exceeded-msg'),
      
      themeToggleBtn: document.getElementById('theme-toggle-btn'),
      profileModalBtn: document.getElementById('profile-modal-btn'),
      profileModal: document.getElementById('profile-modal'),
      closeProfileModal: document.getElementById('close-profile-modal'),
      
      mealManagerModal: document.getElementById('meal-manager-modal'),
      managerTitle: document.getElementById('manager-title'),
      managerCalTotal: document.getElementById('manager-cal-total'),
      closeManagerModalBtn: document.getElementById('close-manager-modal'),
      managerList: document.getElementById('manager-list'),
      
      addMealForm: document.getElementById('add-meal-form'),
      mealNameInput: document.getElementById('meal-name'),
      mealAmountInput: document.getElementById('meal-amount'),
      mealUnitSelect: document.getElementById('meal-unit'),
      mealCaloriesInput: document.getElementById('meal-calories'),
      customDropdown: document.getElementById('custom-dropdown'),
      mealCalcInfo: document.getElementById('meal-calc-info'),
      unitCalDisplay: document.getElementById('unit-cal-display'),
      
      cals: {
        breakfast: document.getElementById('cal-breakfast'),
        lunch: document.getElementById('cal-lunch'),
        dinner: document.getElementById('cal-dinner'),
        snack: document.getElementById('cal-snack')
      },
      
      activityType: document.getElementById('activity-type'),
      startWalkBtn: document.getElementById('start-walk-btn'),
      stopWalkBtn: document.getElementById('stop-walk-btn'),
      liveWalkStats: document.getElementById('live-walk-stats'),
      liveDistance: document.getElementById('live-distance'),
      liveCal: document.getElementById('live-cal'),
      emptyWalks: document.getElementById('empty-walks'),
      
      addToCalendarBtn: document.getElementById('add-to-calendar-btn'),
      reminderTimeInput: document.getElementById('reminder-time'),
      
      settingsGoalInput: document.getElementById('settings-goal'),
      saveSettingsBtn: document.getElementById('save-settings-btn'),
      clearDataBtn: document.getElementById('clear-data-btn'),
      toast: document.getElementById('toast'),
    };

    let currentMealCategory = 'snack';
    const catNames = { breakfast: 'Kahvaltı', lunch: 'Öğle Yemeği', dinner: 'Akşam Yemeği', snack: 'Ara Öğün' };

    function init() {
      loadState();
      checkOnboarding();
      checkMidnightReset();
      updateUI();
      setupEventListeners();
    }

    function checkOnboarding() {
      if (!state.profileSetup) {
        document.getElementById('onboarding').classList.remove('hidden');
      }
    }

    function loadState() {
      const saved = localStorage.getItem('antigravity_state');
      if (saved) state = { ...state, ...JSON.parse(saved) };
      el.settingsGoalInput.value = state.targetCalories;
    }

    function saveState() {
      localStorage.setItem('antigravity_state', JSON.stringify(state));
      updateUI();
    }

    function checkMidnightReset() {
      const today = new Date().toDateString();
      if (state.lastDate !== today) {
        if (state.lastDate !== null) {
          state.consumedCalories = 0;
          state.burnedCalories = 0;
          state.meals = [];
          state.walks = [];
        }
        state.lastDate = today;
        saveState();
      }
    }

    function updateUI() {
      const netTarget = state.targetCalories + state.burnedCalories;
      let remaining = netTarget - state.consumedCalories;
      
      el.consumedMain.textContent = state.consumedCalories;
      el.goalDisplay.textContent = state.targetCalories;
      el.goalExceededMsg.style.display = remaining < 0 ? 'block' : 'none';

      let consumedPercent = state.consumedCalories / netTarget;
      if (consumedPercent > 1) consumedPercent = 1;
      if (isNaN(consumedPercent) || netTarget === 0) consumedPercent = 0;
      
      let netConsumed = state.consumedCalories - state.burnedCalories;
      if (netConsumed < 0) netConsumed = 0;
      
      let netPercent = netConsumed / netTarget;
      if (netPercent > 1) netPercent = 1;
      if (isNaN(netPercent) || netTarget === 0) netPercent = 0;

      const offsetConsumed = RING_CIRCUMFERENCE - (consumedPercent * RING_CIRCUMFERENCE);
      const offsetNet = RING_CIRCUMFERENCE - (netPercent * RING_CIRCUMFERENCE);

      el.ringBurned.style.strokeDashoffset = offsetConsumed;
      el.ring.style.strokeDashoffset = offsetNet;

      let categoryTotals = { breakfast: 0, lunch: 0, dinner: 0, snack: 0 };
      state.meals.forEach(meal => {
        const cat = meal.category || 'snack';
        categoryTotals[cat] += meal.calories;
      });

      Object.keys(categoryTotals).forEach(cat => {
        if(el.cals[cat]) el.cals[cat].textContent = categoryTotals[cat] + ' kcal';
      });

      el.emptyWalks.style.display = (state.walks && state.walks.length > 0) ? 'none' : 'block';
    }

    function openManagerModal(cat) {
      currentMealCategory = cat;
      el.managerTitle.textContent = catNames[cat];
      
      let total = 0;
      el.managerList.innerHTML = '';
      
      const catMeals = state.meals.filter(m => (m.category || 'snack') === cat);
      catMeals.forEach(meal => {
        total += meal.calories;
        const li = document.createElement('li');
        li.className = 'meal-item';
        li.innerHTML = `
          <div class="meal-info">
            <div class="meal-name">${escapeHTML(meal.name)}</div>
            <div class="meal-cal">${meal.calories} kcal</div>
          </div>
          <button class="delete-btn" onclick="deleteMeal('${meal.id}', '${cat}')">&times;</button>
        `;
        el.managerList.appendChild(li);
      });
      
      if(catMeals.length === 0) {
         el.managerList.innerHTML = '<li class="empty-state" style="padding: 10px;">Bu öğün için henüz kayıt yok.</li>';
      }
      
      el.managerCalTotal.textContent = total + ' kcal';
      el.mealManagerModal.classList.remove('hidden');
    }

    window.deleteMeal = function(id, cat) {
      const idx = state.meals.findIndex(m => m.id === id);
      if (idx !== -1) {
        state.consumedCalories -= state.meals[idx].calories;
        if(state.consumedCalories < 0) state.consumedCalories = 0;
        state.meals.splice(idx, 1);
        saveState();
        openManagerModal(cat); // refresh list
      }
    };

    function showToast(msg) {
      el.toast.textContent = msg;
      el.toast.classList.add('show');
      setTimeout(() => el.toast.classList.remove('show'), 3000);
    }

    function escapeHTML(str) {
      return str.replace(/[&<>'"]/g, tag => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;' }[tag]));
    }

    function setupEventListeners() {
      // Theme Toggle Logic
      let currentTheme = localStorage.getItem('antigravity_theme') || 'light';
      document.body.setAttribute('data-theme', currentTheme);
      const svg_moon = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>';
      const svg_sun = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>';
      const themeIconContainer = document.getElementById('theme-icon-container');
      themeIconContainer.innerHTML = currentTheme === 'light' ? svg_moon : svg_sun;

      el.themeToggleBtn.addEventListener('click', () => {
        currentTheme = currentTheme === 'light' ? 'dark' : 'light';
        document.body.setAttribute('data-theme', currentTheme);
        themeIconContainer.innerHTML = currentTheme === 'light' ? svg_moon : svg_sun;
        localStorage.setItem('antigravity_theme', currentTheme);
      });

      // Profile Modal
      el.profileModalBtn.addEventListener('click', () => el.profileModal.classList.remove('hidden'));
      el.closeProfileModal.addEventListener('click', () => el.profileModal.classList.add('hidden'));

      // Dashboard Meal Buttons
      document.querySelectorAll('.meal-dash-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          openManagerModal(btn.getAttribute('data-category'));
        });
      });
      el.closeManagerModalBtn.addEventListener('click', () => {
        el.mealManagerModal.classList.add('hidden');
      });

      // Meal Calc and Dropdown
      const renderDropdown = (query) => {
        el.customDropdown.innerHTML = '';
        if (!query) { el.customDropdown.style.display = 'none'; return; }
        const q = query.toLowerCase();
        const results = foodDatabase.filter(f => f.name.toLowerCase().includes(q));
        if (results.length === 0) { el.customDropdown.style.display = 'none'; return; }

        const grouped = {};
        results.forEach(f => {
          if (!grouped[f.type]) grouped[f.type] = [];
          grouped[f.type].push(f);
        });

        Object.keys(grouped).forEach(type => {
          const title = document.createElement('div');
          title.className = 'dropdown-group-title'; title.textContent = type;
          el.customDropdown.appendChild(title);
          grouped[type].forEach(f => {
            const item = document.createElement('div');
            item.className = 'dropdown-item'; item.textContent = f.name;
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

      const calculateMealCals = () => {
        const name = el.mealNameInput.value.trim();
        const amount = parseFloat(el.mealAmountInput.value);
        const unitName = el.mealUnitSelect.options[el.mealUnitSelect.selectedIndex].text;
        const food = foodDatabase.find(f => f.name === name);
        
        if (food) {
          el.mealCalcInfo.style.display = 'block';
          if (amount > 0) {
            let totalWeight = amount;
            if (unitName === 'Gram / ml') totalWeight = amount;
            else if (unitName === 'Su Bardağı') totalWeight = amount * 200;
            else if (unitName === 'Çay Bardağı') totalWeight = amount * 100;
            else if (unitName === 'Porsiyon') totalWeight = amount * (food.porsiyon || 150);
            else if (unitName === 'Adet') totalWeight = amount * (food.adet || 100);
            else if (unitName === 'Dilim') totalWeight = amount * (food.dilim || food.adet || 100);
            
            const calculatedCal = Math.round((food.cal * totalWeight) / 100);
            el.mealCaloriesInput.value = calculatedCal;
            
            if (unitName === 'Adet') {
              const perAdet = Math.round((food.cal * (food.adet || 100)) / 100);
              el.unitCalDisplay.innerHTML = `1 adeti (~${food.adet || 100}g) <b>${perAdet}</b>`;
            } else if (unitName === 'Dilim') {
              const perDilim = Math.round((food.cal * (food.dilim || food.adet || 100)) / 100);
              el.unitCalDisplay.innerHTML = `1 dilimi (~${food.dilim || food.adet || 100}g) <b>${perDilim}</b>`;
            } else if (unitName === 'Porsiyon') {
              const perPor = Math.round((food.cal * (food.porsiyon || 150)) / 100);
              el.unitCalDisplay.innerHTML = `1 porsiyonu (~${food.porsiyon || 150}g) <b>${perPor}</b>`;
            } else {
              el.unitCalDisplay.innerHTML = `100 gramı <b>${food.cal}</b>`;
            }
          } else {
            el.unitCalDisplay.innerHTML = `100 gramı <b>${food.cal}</b>`;
            el.mealCaloriesInput.value = '';
          }
        } else {
          el.mealCalcInfo.style.display = 'none';
        }
      };

      el.mealAmountInput.addEventListener('input', calculateMealCals);
      el.mealUnitSelect.addEventListener('change', calculateMealCals);

      el.addMealForm.addEventListener('submit', (e) => {
        e.preventDefault();
        let name = el.mealNameInput.value.trim();
        const amount = parseFloat(el.mealAmountInput.value.trim());
        const cal = parseInt(el.mealCaloriesInput.value, 10);
        
        if (name && cal > 0) {
          if (amount) {
            const unitText = el.mealUnitSelect.options[el.mealUnitSelect.selectedIndex].text;
            const unitSuffix = unitText === 'Gram / ml' ? 'g' : (unitText === 'Adet' ? ' adet' : ` ${unitText}`);
            name += ` (${amount}${unitSuffix})`;
          }
          state.meals.push({
            id: Date.now().toString(), name, calories: cal, category: currentMealCategory, time: new Date().toISOString()
          });
          state.consumedCalories += cal;
          
          pulseRing();
          el.mealNameInput.value = ''; el.mealAmountInput.value = ''; el.mealCaloriesInput.value = '';
          el.mealCalcInfo.style.display = 'none';
          saveState();
          showToast('Öğün eklendi');
          openManagerModal(currentMealCategory);
        }
      });

      function pulseRing() {
        el.ring.parentElement.style.transform = 'scale(1.05)';
        setTimeout(() => el.ring.parentElement.style.transform = 'scale(1)', 200);
      }

      // Add to Calendar Integration
      el.addToCalendarBtn.addEventListener('click', () => {
        const time = el.reminderTimeInput.value;
        if(!time) return;
        const [hours, minutes] = time.split(':');
        
        const now = new Date();
        now.setHours(hours, minutes, 0);
        
        const formatICSDate = (date) => {
          return date.toISOString().replace(/[-:]/g, '').split('.')[0] + 'Z';
        };
        
        const dtstart = formatICSDate(now);
        const dtend = formatICSDate(new Date(now.getTime() + 60 * 60 * 1000));
        
        const icsContent = `BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//METRA//Spor Asistanı//TR
BEGIN:VEVENT
UID:${Date.now()}@metra.app
DTSTAMP:${formatICSDate(new Date())}
DTSTART:${dtstart}
DTEND:${dtend}
RRULE:FREQ=DAILY
SUMMARY:🏃‍♂️ METRA Antrenman Vakti!
DESCRIPTION:Günlük egzersiz ve su hedeflerini tamamlamayı unutma.
BEGIN:VALARM
TRIGGER:-PT0M
ACTION:DISPLAY
DESCRIPTION:Reminder
END:VALARM
END:VEVENT
END:VCALENDAR`;

        const blob = new Blob([icsContent], { type: 'text/calendar;charset=utf-8' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'metra_antrenman.ics';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
        
        showToast('Takvim dosyası indirildi!');
      });

      // Settings and Profile
      document.getElementById('onboarding-form').addEventListener('submit', (e) => {
        e.preventDefault();
        state.gender = document.getElementById('ob-gender').value;
        state.age = parseInt(document.getElementById('ob-age').value, 10);
        state.height = parseInt(document.getElementById('ob-height').value, 10);
        state.userWeight = parseFloat(document.getElementById('ob-weight').value);
        state.activityLevel = parseFloat(document.getElementById('ob-activity').value);
        
        let bmr = state.gender === 'male' 
          ? (10 * state.userWeight) + (6.25 * state.height) - (5 * state.age) + 5
          : (10 * state.userWeight) + (6.25 * state.height) - (5 * state.age) - 161;
        
        state.targetCalories = Math.round(bmr * state.activityLevel);
        state.profileSetup = true;
        el.settingsGoalInput.value = state.targetCalories;
        
        saveState();
        document.getElementById('onboarding').classList.add('hidden');
        showToast('Profil oluşturuldu!');
      });

      el.saveSettingsBtn.addEventListener('click', () => {
        const target = parseInt(el.settingsGoalInput.value, 10);
        if (target >= 500) {
          state.targetCalories = target;
          saveState();
          showToast('Hedef güncellendi');
        }
      });
      
      el.clearDataBtn.addEventListener('click', () => {
        if(confirm('Tüm verilerin silinecek. Emin misin?')) {
          localStorage.removeItem('antigravity_state');
          location.reload();
        }
      });

      // Walk / GPS Logic
      let map, marker, pathLine;
      let walkInterval, watchId;
      let isWalking = false;
      let walkDistance = 0;
      let walkSeconds = 0;
      let walkPath = [];
      
      const activityMets = { walk: 3.5, run: 8.0, bike: 6.0 };

      el.startWalkBtn.addEventListener('click', () => {
        if (isWalking) return;
        if (!navigator.geolocation) { alert('Tarayıcın GPS desteklemiyor.'); return; }
        
        isWalking = true;
        walkDistance = 0;
        walkSeconds = 0;
        walkPath = [];
        
        el.liveDistance.textContent = '0.00';
        el.liveCal.textContent = '0';
        el.liveWalkStats.style.display = 'flex';
        el.startWalkBtn.style.display = 'none';
        el.stopWalkBtn.style.display = 'block';
        el.activityType.disabled = true;
        
        const mapContainer = document.getElementById('map');
        mapContainer.style.display = 'block';
        
        if (!map) {
          map = L.map('map').setView([41.0082, 28.9784], 15);
          L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
            attribution: '&copy; OpenStreetMap'
          }).addTo(map);
        }
        
        if (pathLine) map.removeLayer(pathLine);
        if (marker) map.removeLayer(marker);
        
        pathLine = L.polyline([], {color: '#00F5C3', weight: 4}).addTo(map);
        marker = L.circleMarker([0,0], {radius: 6, color: '#FF4D4D', fillColor: '#FF4D4D', fillOpacity: 1}).addTo(map);

        navigator.geolocation.getCurrentPosition(pos => {
          const latlng = [pos.coords.latitude, pos.coords.longitude];
          map.setView(latlng, 17);
          marker.setLatLng(latlng);
          walkPath.push(latlng);
          pathLine.addLatLng(latlng);
        });

        watchId = navigator.geolocation.watchPosition(pos => {
          const newLatLng = [pos.coords.latitude, pos.coords.longitude];
          if (walkPath.length > 0) {
            const prev = walkPath[walkPath.length - 1];
            walkDistance += map.distance(prev, newLatLng) / 1000;
          }
          walkPath.push(newLatLng);
          pathLine.addLatLng(newLatLng);
          marker.setLatLng(newLatLng);
          map.panTo(newLatLng);
          
          el.liveDistance.textContent = walkDistance.toFixed(2);
        }, err => console.error(err), { enableHighAccuracy: true });

        walkInterval = setInterval(() => {
          walkSeconds++;
          const type = el.activityType.value;
          const met = activityMets[type] || 3.5;
          const hours = walkSeconds / 3600;
          const calBurned = Math.round(met * state.userWeight * hours);
          el.liveCal.textContent = calBurned;
        }, 1000);
      });

      el.stopWalkBtn.addEventListener('click', () => {
        if (!isWalking) return;
        isWalking = false;
        
        navigator.geolocation.clearWatch(watchId);
        clearInterval(walkInterval);
        
        el.startWalkBtn.style.display = 'block';
        el.stopWalkBtn.style.display = 'none';
        el.activityType.disabled = false;
        
        const type = el.activityType.value;
        const met = activityMets[type] || 3.5;
        const currentWalkCal = Math.round(met * state.userWeight * (walkSeconds / 3600));
        
        if (currentWalkCal > 0 || walkDistance > 0) {
          state.burnedCalories += currentWalkCal;
          const typeNames = { walk: '🏃‍♂️ Yürüyüş', run: '🏃‍♀️ Koşu', bike: '🚴 Bisiklet' };
          const currentActivityName = typeNames[type] || 'Aktivite';
          
          state.walks.push({
            id: Date.now().toString(), name: currentActivityName, calories: currentWalkCal, distance: walkDistance.toFixed(2), time: new Date().toISOString()
          });
          
          pulseRing();
          saveState();
          showToast('Egzersiz kaydedildi 💪');
        }
      });
    }

    window.onload = init;
  </script>
</body>
</html>
"""

body_html = body_html.replace('PLACEHOLDER_DB', food_db)

new_content = head + style + "\n" + body_html

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("V7 Dashboard architecture generated!")
