
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

    let state = {
      profileSetup: false, gender: 'male', age: 25, height: 175, activityLevel: 1.55,
      targetCalories: 2000, consumedCalories: 0, burnedCalories: 0, meals: [], walks: [],
      lastDate: null, userWeight: 70
    };

    const RING_CIRCUMFERENCE = 2 * Math.PI * 96;

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
      gpsStartOverlay: document.getElementById('gps-overlay-start'),
      gpsStopOverlay: document.getElementById('gps-overlay-stop'),
      gpsStatsOverlay: document.getElementById('gps-overlay-stats'),
      
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
      el.ring.style.strokeDasharray = RING_CIRCUMFERENCE;
      el.ring.style.strokeDashoffset = RING_CIRCUMFERENCE;
      el.ringBurned.style.strokeDasharray = RING_CIRCUMFERENCE;
      el.ringBurned.style.strokeDashoffset = RING_CIRCUMFERENCE;
      
      loadState();
      checkOnboarding();
      checkMidnightReset();
      setTimeout(updateUI, 50);
      setupEventListeners();
      initMapPlaceholder();
    }
    
    
    let map, marker, pathLine;
    function initMapPlaceholder() {
      if (!map) {
        map = L.map('map', { zoomControl: false, attributionControl: false }).setView([41.0082, 28.9784], 12);
        L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png').addTo(map);
        // Let it be a dark beautiful background map of Istanbul by default
      }
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
        if(el.cals[cat]) el.cals[cat].textContent = categoryTotals[cat];
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
      if (!localStorage.getItem('v9_theme_reset')) {
        localStorage.setItem('antigravity_theme', 'light');
        localStorage.setItem('v9_theme_reset', 'true');
      }
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
              
              // Smart Unit Selection
              let unitToSelect = '1'; // Default Gram/ml
              if (f.type === 'İçecekler') unitToSelect = '200'; // Su Bardağı
              else if (f.type === 'Meyveler') unitToSelect = '1'; // Adet (we use value 1 for Adet but select by text below)
              else if (f.type === 'Pizza' || f.type === 'Hamur İşi' || f.name.includes('Börek') || f.name.includes('Ekmek')) unitToSelect = 'Dilim';
              else if (f.type === 'Çorba' || f.type === 'Salata' || f.type === 'Mezeler' || f.type === 'Ana Yemekler') unitToSelect = '150'; // Porsiyon
              else if (f.adet) unitToSelect = 'Adet';
              
              if (unitToSelect === 'Adet' || unitToSelect === 'Dilim') {
                for(let opt of el.mealUnitSelect.options) {
                  if(opt.text === unitToSelect) { opt.selected = true; break; }
                }
                el.mealAmountInput.value = 1;
              } else {
                for(let opt of el.mealUnitSelect.options) {
                  if(opt.value === unitToSelect) { opt.selected = true; break; }
                }
                if (unitToSelect === '1') el.mealAmountInput.value = 100;
                else el.mealAmountInput.value = 1;
              }
              
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
      
      let walkInterval, watchId;
      let isWalking = false;
      let walkDistance = 0;
      let walkSeconds = 0;
      let walkPath = [];
      
      const activityMets = { walk: 3.5, run: 8.0, bike: 6.0 };

      document.getElementById('close-summary-btn').addEventListener('click', () => {
        document.getElementById('activity-summary-modal').classList.add('hidden');
      });
      document.getElementById('share-summary-btn').addEventListener('click', () => {
        const card = document.getElementById('summary-card');
        html2canvas(card, {backgroundColor: null}).then(canvas => {
          const link = document.createElement('a');
          link.download = 'metra_egzersiz.png';
          link.href = canvas.toDataURL();
          link.click();
        });
      });
      
      el.startWalkBtn.addEventListener('click', () => {
        if (isWalking) return;
        if (!navigator.geolocation) { alert('Tarayıcın GPS desteklemiyor.'); return; }
        
        isWalking = true;
        walkDistance = 0;
        walkSeconds = 0;
        walkPath = [];
        
        el.liveDistance.textContent = '0.00';
        el.liveCal.textContent = '0';
        el.gpsStatsOverlay.style.display = 'block';
        el.gpsStartOverlay.style.display = 'none';
        el.gpsStopOverlay.style.display = 'block';
        el.activityType.disabled = true;
        
        // Map is already initialized by initMapPlaceholder
        
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
        
        el.gpsStartOverlay.style.display = 'block';
        el.gpsStopOverlay.style.display = 'none';
        el.gpsStatsOverlay.style.display = 'none';
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
  