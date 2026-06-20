import re
import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Head
head_target = """<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@500;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  <style>"""
head_replacement = """<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@500;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin=""/>
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>
  <style>"""
content = content.replace(head_target, head_replacement)

# 2. CSS
css_target = """    .setting-group {
      margin-bottom: 24px;
    }

  </style>"""
css_replacement = """    .setting-group {
      margin-bottom: 24px;
    }

    /* Map & Onboarding Styles */
    #walk-map {
      height: 300px;
      width: 100%;
      border-radius: 16px;
      margin-bottom: 24px;
      z-index: 1;
      border: 2px solid var(--divider-color);
    }
    
    .onboarding-overlay {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-color: var(--bg-color);
      z-index: 1000;
      display: flex;
      flex-direction: column;
      padding: 24px;
      overflow-y: auto;
    }
    
    .onboarding-overlay.hidden {
      display: none;
    }
    
    .onboarding-title {
      font-size: 2rem;
      color: var(--accent-color);
      margin-bottom: 8px;
    }

    .tracking-stats {
      display: flex;
      justify-content: space-between;
      margin-top: 16px;
      margin-bottom: 24px;
      text-align: center;
    }

    .tracking-stats .stat-item {
      flex: 1;
    }

    .tracking-stats .value {
      font-family: var(--font-heading);
      font-size: 1.5rem;
      font-weight: 700;
      color: var(--accent-color);
    }
  </style>"""
content = content.replace(css_target, css_replacement)

# 3. Meal form
meal_target = """        <div style="display: flex; gap: 16px;">
          <div class="input-group" style="flex: 1;">
            <label for="meal-amount">Miktar (Gram)</label>
            <input type="number" id="meal-amount" placeholder="Örn: 100" min="1">
          </div>
          <div class="input-group" style="flex: 1;">
            <label for="meal-calories">Kalori (kcal)</label>
            <input type="number" id="meal-calories" placeholder="Örn: 350" required min="1">
          </div>
        </div>"""
meal_replacement = """        <div style="display: flex; gap: 16px;">
          <div class="input-group" style="flex: 1.5;">
            <label for="meal-amount">Miktar / Birim</label>
            <div style="display: flex; gap: 8px;">
              <input type="number" id="meal-amount" placeholder="100" min="1" style="flex: 1;">
              <select id="meal-unit" style="flex: 1.5; padding-left: 8px; padding-right: 8px; font-size: 0.875rem;">
                <option value="1">Gram / ml</option>
                <option value="200">Su Bardağı</option>
                <option value="100">Çay Bardağı</option>
                <option value="150">Porsiyon</option>
              </select>
            </div>
          </div>
          <div class="input-group" style="flex: 1;">
            <label for="meal-calories">Kalori (kcal)</label>
            <input type="number" id="meal-calories" placeholder="Örn: 350" required min="1">
          </div>
        </div>"""
content = content.replace(meal_target, meal_replacement)

# 4. Walk form
walk_target = re.compile(r'<!-- Tab 2: Yürüyüş \(Walk\) -->.*?</section>', re.DOTALL)
walk_replacement = """<!-- Tab 2: Yürüyüş (Walk) -->
    <section id="tab-walk" class="tab-content">
      <h2 class="section-title">Canlı Yürüyüş Takibi</h2>
      <p class="info-text" style="margin-bottom: 24px;">GPS ile yürüdüğün mesafeyi takip et ve yaktığın kaloriyi net hedefine ekle.</p>
      
      <div id="walk-map-container" style="display: none;">
        <div id="walk-map"></div>
        <div id="tracking-ui">
          <div class="tracking-stats">
            <div class="stat-item">
              <div class="value" id="track-time">00:00</div>
              <div class="label">Süre</div>
            </div>
            <div class="stat-item">
              <div class="value" id="track-dist">0.00</div>
              <div class="label">Mesafe (km)</div>
            </div>
            <div class="stat-item">
              <div class="value" id="track-cal">0</div>
              <div class="label">Kcal</div>
            </div>
          </div>
        </div>
      </div>

      <button type="button" id="start-walk-btn">Yürüyüşe Başla (GPS)</button>
      <button type="button" id="stop-walk-btn" style="display: none; background-color: var(--error-color); margin-top: 16px;">Yürüyüşü Bitir ve Kaydet</button>
      
      <div id="walk-result-container" style="display: none;">
        <div id="walk-result">0</div>
        <div class="info-text">Son Yürüyüşten Yakılan</div>
      </div>
      <div id="empty-walks" class="empty-state" style="margin-top: 24px;">
        Yürüyüş kaydın yok, hadi başla!
      </div>
    </section>"""
content = walk_target.sub(walk_replacement, content)

# 5. Onboarding overlay
toast_target = """  <div id="toast" class="toast"></div>"""
toast_replacement = """  <div id="toast" class="toast"></div>

  <div id="onboarding" class="onboarding-overlay hidden">
    <h1 class="onboarding-title">Antigravity'ye Hoş Geldin</h1>
    <p class="info-text" style="margin-bottom: 32px;">Sana özel günlük kalori hedefini hesaplayabilmemiz için birkaç bilgiye ihtiyacımız var.</p>
    
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
      <button type="submit" style="margin-top: 16px;">Profilimi Oluştur</button>
    </form>
  </div>"""
content = content.replace(toast_target, toast_replacement)

# 6. JS State
state_target = """    let state = {
      targetCalories: 2000,
      consumedCalories: 0,
      burnedCalories: 0,
      meals: [],
      walks: [],
      lastDate: null,
      reminderTime: '18:30',
      reminderEnabled: false,
      userWeight: 70
    };"""
state_replacement = """    let state = {
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
    };"""
content = content.replace(state_target, state_replacement)

# 7. JS Elements
el_target = re.compile(r'      addMealForm: document.getElementById\(\'add-meal-form\'\).*?emptyWalks: document.getElementById\(\'empty-walks\'\),', re.DOTALL)
el_replacement = """      addMealForm: document.getElementById('add-meal-form'),
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
      walkResultContainer: document.getElementById('walk-result-container'),
      walkResult: document.getElementById('walk-result'),
      emptyWalks: document.getElementById('empty-walks'),"""
content = el_target.sub(el_replacement, content)

# 8. JS Init & Onboarding logic
init_target = """    // Initialization
    function init() {
      populateFoodList();
      loadState();
      checkMidnightReset();"""
init_replacement = """    // Initialization
    function init() {
      populateFoodList();
      loadState();
      checkOnboarding();
      checkMidnightReset();"""
content = content.replace(init_target, init_replacement)

logic_target = """    function loadState() {"""
logic_replacement = """    // GPS Tracking variables
    let watchId = null;
    let walkStartTime = null;
    let walkPoints = [];
    let walkMapObj = null;
    let walkPolyline = null;
    let totalDistanceKm = 0;
    let currentWalkCal = 0;
    let trackInterval = null;

    function checkOnboarding() {
      if (!state.profileSetup) {
        document.getElementById('onboarding').classList.remove('hidden');
      }
    }

    document.getElementById('onboarding-form').addEventListener('submit', (e) => {
      e.preventDefault();
      state.gender = document.getElementById('ob-gender').value;
      state.age = parseInt(document.getElementById('ob-age').value, 10);
      state.userWeight = parseFloat(document.getElementById('ob-weight').value);
      state.height = parseInt(document.getElementById('ob-height').value, 10);
      state.activityLevel = parseFloat(document.getElementById('ob-activity').value);
      
      // Mifflin-St Jeor Formula
      let bmr = 10 * state.userWeight + 6.25 * state.height - 5 * state.age;
      if (state.gender === 'male') {
        bmr += 5;
      } else {
        bmr -= 161;
      }
      
      state.targetCalories = Math.round(bmr * state.activityLevel);
      state.profileSetup = true;
      el.settingsGoalInput.value = state.targetCalories;
      
      saveState();
      document.getElementById('onboarding').classList.add('hidden');
      showToast('Profil oluşturuldu!');
    });

    function loadState() {"""
content = content.replace(logic_target, logic_replacement)

# 9. Walk Logic Event Listeners replacement
ev_target = re.compile(r'      // Walk calculator.*?emptyWalks\.style\.display = state\.walks\.length > 0 \? \'none\' : \'block\';\n        }\n      }\);\n', re.DOTALL)
ev_replacement = """      // Walk map logic
      el.startWalkBtn.addEventListener('click', () => {
        if (!("geolocation" in navigator)) {
          showToast("Tarayıcınız GPS desteklemiyor.");
          return;
        }
        
        el.walkMapContainer.style.display = 'block';
        el.startWalkBtn.style.display = 'none';
        el.stopWalkBtn.style.display = 'block';
        
        if (!walkMapObj) {
          walkMapObj = L.map('walk-map').setView([41.0082, 28.9784], 15);
          L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap'
          }).addTo(walkMapObj);
          walkPolyline = L.polyline([], {color: 'var(--accent-color)', weight: 5}).addTo(walkMapObj);
        }
        setTimeout(() => walkMapObj.invalidateSize(), 100);

        walkPoints = [];
        totalDistanceKm = 0;
        currentWalkCal = 0;
        walkStartTime = new Date();
        walkPolyline.setLatLngs([]);
        
        el.trackTime.textContent = "00:00";
        el.trackDist.textContent = "0.00";
        el.trackCal.textContent = "0";

        trackInterval = setInterval(() => {
          if (!walkStartTime) return;
          const diffSecs = Math.floor((new Date() - walkStartTime) / 1000);
          const mins = Math.floor(diffSecs / 60);
          const secs = diffSecs % 60;
          el.trackTime.textContent = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
          
          const diffHours = diffSecs / 3600;
          const speedKmh = diffHours > 0 ? (totalDistanceKm / diffHours) : 0;
          
          let met = 2.8;
          if (speedKmh > 6) met = 4.3;
          else if (speedKmh > 4) met = 3.5;
          
          currentWalkCal = Math.round(met * state.userWeight * diffHours);
          el.trackCal.textContent = currentWalkCal;
        }, 1000);

        watchId = navigator.geolocation.watchPosition(
          (position) => {
            const lat = position.coords.latitude;
            const lng = position.coords.longitude;
            const newPoint = L.latLng(lat, lng);
            
            if (walkPoints.length > 0) {
              const lastPoint = walkPoints[walkPoints.length - 1];
              totalDistanceKm += (lastPoint.distanceTo(newPoint) / 1000);
            }
            
            walkPoints.push(newPoint);
            walkPolyline.addLatLng(newPoint);
            walkMapObj.panTo(newPoint);
            el.trackDist.textContent = totalDistanceKm.toFixed(2);
          },
          (err) => {
            console.error(err);
            showToast("Konum alınamadı. İzin verildiğine emin olun.");
          },
          { enableHighAccuracy: true, maximumAge: 10000, timeout: 5000 }
        );
      });

      el.stopWalkBtn.addEventListener('click', () => {
        if (watchId) navigator.geolocation.clearWatch(watchId);
        clearInterval(trackInterval);
        
        el.startWalkBtn.style.display = 'block';
        el.stopWalkBtn.style.display = 'none';
        el.walkMapContainer.style.display = 'none';
        
        if (currentWalkCal > 0) {
          state.burnedCalories += currentWalkCal;
          state.walks = state.walks || [];
          state.walks.push({
            id: Date.now().toString(),
            calories: currentWalkCal,
            distance: totalDistanceKm.toFixed(2),
            time: new Date().toISOString()
          });
          
          pulseRing();
          saveState();
          showToast('Yürüyüş kaydedildi 💪');
          
          el.walkResult.textContent = currentWalkCal;
          el.walkResultContainer.style.display = 'block';
          el.emptyWalks.style.display = 'none';
        }
      });
"""
content = ev_target.sub(ev_replacement, content)

# 10. Meal Calculation Logic
meal_calc_target = """      // Meal auto calculation
      const calculateMealCals = () => {
        const name = el.mealNameInput.value.trim();
        const amount = parseFloat(el.mealAmountInput.value);
        const food = foodDatabase.find(f => f.name === name);
        
        if (food) {
          el.mealCalcInfo.style.display = 'block';
          el.unitCalDisplay.textContent = food.cal;
          if (amount > 0) {
            el.mealCaloriesInput.value = Math.round((food.cal * amount) / 100);
          }
        } else {
          el.mealCalcInfo.style.display = 'none';
        }
      };

      el.mealNameInput.addEventListener('input', calculateMealCals);
      el.mealAmountInput.addEventListener('input', calculateMealCals);"""
meal_calc_replacement = """      // Meal auto calculation
      const calculateMealCals = () => {
        const name = el.mealNameInput.value.trim();
        const amount = parseFloat(el.mealAmountInput.value);
        const unitMultiplier = parseFloat(el.mealUnitSelect.value);
        const food = foodDatabase.find(f => f.name === name);
        
        if (food) {
          el.mealCalcInfo.style.display = 'block';
          el.unitCalDisplay.textContent = food.cal;
          if (amount > 0) {
            const totalWeight = amount * unitMultiplier;
            el.mealCaloriesInput.value = Math.round((food.cal * totalWeight) / 100);
          }
        } else {
          el.mealCalcInfo.style.display = 'none';
        }
      };

      el.mealNameInput.addEventListener('input', calculateMealCals);
      el.mealAmountInput.addEventListener('input', calculateMealCals);
      el.mealUnitSelect.addEventListener('change', calculateMealCals);"""
content = content.replace(meal_calc_target, meal_calc_replacement)

# 11. Meal submit
meal_submit_target = """        if (name && cal > 0) {
          if (amount) name += ` (${amount}g)`;"""
meal_submit_replacement = """        if (name && cal > 0) {
          if (amount) {
            const unitMultiplier = parseFloat(el.mealUnitSelect.value);
            const unitText = el.mealUnitSelect.options[el.mealUnitSelect.selectedIndex].text;
            const unitSuffix = unitMultiplier === 1 ? 'g' : ` ${unitText}`;
            name += ` (${amount}${unitSuffix})`;
          }"""
content = content.replace(meal_submit_target, meal_submit_replacement)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Update complete")
