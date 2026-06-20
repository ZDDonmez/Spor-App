import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the GPS Section HTML
gps_target = """    <!-- Middle Section: Exercise & GPS -->
    <div class="glass-card">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
        <h2 class="section-title" style="margin: 0; font-size: 1.2rem;">Egzersiz ve GPS</h2>
        <select id="activity-type" style="padding: 6px 12px; border-radius: 20px; border: 1px solid var(--surface-border); background: var(--surface-color); color: var(--text-color); font-family: var(--font-body); font-size: 0.9rem; outline: none; -webkit-appearance: none; cursor: pointer;">
          <option value="walk">Yürüyüş</option>
          <option value="run">Koşu</option>
          <option value="bike">Bisiklet</option>
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
    </div>"""

gps_replacement = """    <!-- Middle Section: Exercise & GPS -->
    <div class="glass-card" style="padding: 0; overflow: hidden; display: flex; flex-direction: column;">
      <div style="padding: 16px 20px; background: var(--surface-color); border-bottom: 1px solid var(--surface-border); display: flex; justify-content: space-between; align-items: center; z-index: 10;">
        <h2 class="section-title" style="margin: 0; font-size: 1.1rem; gap: 6px;">🌍 Canlı Rota Takibi</h2>
        <select id="activity-type" style="padding: 4px 10px; border-radius: 20px; border: 1px solid var(--surface-border); background: var(--bg-color); color: var(--accent-color); font-family: var(--font-body); font-weight: 600; font-size: 0.85rem; outline: none; -webkit-appearance: none; cursor: pointer;">
          <option value="walk">Yürüyüş</option>
          <option value="run">Koşu</option>
          <option value="bike">Bisiklet</option>
        </select>
      </div>
      
      <div style="position: relative; width: 100%; height: 260px;">
        <div id="map" style="width: 100%; height: 100%; background: #111; z-index: 1;"></div>
        
        <div id="gps-overlay-start" style="position: absolute; bottom: 20px; left: 50%; transform: translateX(-50%); z-index: 10; width: 80%;">
          <button type="button" id="start-walk-btn" style="box-shadow: 0 8px 24px rgba(0,0,0,0.4); font-size: 1.1rem; letter-spacing: 1px;">📡 BAŞLA</button>
        </div>
        
        <div id="gps-overlay-stats" style="position: absolute; top: 0; left: 0; width: 100%; padding: 12px; background: linear-gradient(to bottom, rgba(0,0,0,0.8), transparent); z-index: 10; display: none;">
          <div class="stats-row" id="live-walk-stats" style="margin-bottom: 0;">
            <div class="stat-item">
              <div class="value" id="live-distance" style="color: #fff; text-shadow: 0 2px 4px rgba(0,0,0,0.5);">0.00</div>
              <div class="label" style="color: rgba(255,255,255,0.8);">Mesafe (km)</div>
            </div>
            <div class="stat-item">
              <div class="value" id="live-cal" style="color: var(--accent-color); text-shadow: 0 2px 4px rgba(0,0,0,0.5);">0</div>
              <div class="label" style="color: rgba(255,255,255,0.8);">Yakılan</div>
            </div>
          </div>
        </div>
        
        <div id="gps-overlay-stop" style="position: absolute; bottom: 20px; left: 50%; transform: translateX(-50%); z-index: 10; width: 80%; display: none;">
          <button type="button" id="stop-walk-btn" class="danger-btn" style="box-shadow: 0 8px 24px rgba(239, 68, 68, 0.4); font-size: 1.1rem; letter-spacing: 1px;">Egzersizi Bitir</button>
        </div>
      </div>
    </div>"""
content = content.replace(gps_target, gps_replacement)


# 2. Update JS for Map Initialization on Load
init_js_target = """    function init() {
      el.ring.style.strokeDasharray = RING_CIRCUMFERENCE;
      el.ring.style.strokeDashoffset = RING_CIRCUMFERENCE;
      el.ringBurned.style.strokeDasharray = RING_CIRCUMFERENCE;
      el.ringBurned.style.strokeDashoffset = RING_CIRCUMFERENCE;
      
      loadState();
      checkOnboarding();
      checkMidnightReset();
      setTimeout(updateUI, 50); // slight delay to trigger CSS transition gliding
      setupEventListeners();
    }"""
init_js_replacement = """    function init() {
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
    }"""
content = content.replace(init_js_target, init_js_replacement)

# Update Map references in startWalkBtn logic
map_logic_target = """        if (!map) {
          map = L.map('map').setView([41.0082, 28.9784], 15);
          L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
            attribution: '&copy; OpenStreetMap'
          }).addTo(map);
        }"""
map_logic_replacement = """        // Map is already initialized by initMapPlaceholder"""
content = content.replace(map_logic_target, map_logic_replacement)


# Also we need to fix elements definitions in JS
el_target = """      liveCal: document.getElementById('live-cal'),
      emptyWalks: document.getElementById('empty-walks'),"""
el_replacement = """      liveCal: document.getElementById('live-cal'),
      gpsStartOverlay: document.getElementById('gps-overlay-start'),
      gpsStopOverlay: document.getElementById('gps-overlay-stop'),
      gpsStatsOverlay: document.getElementById('gps-overlay-stats'),"""
content = content.replace(el_target, el_replacement)

# Update the display logic in start/stop
start_logic_target = """        el.liveWalkStats.style.display = 'flex';
        el.startWalkBtn.style.display = 'none';
        el.stopWalkBtn.style.display = 'block';
        el.activityType.disabled = true;
        
        const mapContainer = document.getElementById('map');
        mapContainer.style.display = 'block';"""
start_logic_replacement = """        el.gpsStatsOverlay.style.display = 'block';
        el.gpsStartOverlay.style.display = 'none';
        el.gpsStopOverlay.style.display = 'block';
        el.activityType.disabled = true;"""
content = content.replace(start_logic_target, start_logic_replacement)

stop_logic_target = """        el.startWalkBtn.style.display = 'block';
        el.stopWalkBtn.style.display = 'none';
        el.activityType.disabled = false;"""
stop_logic_replacement = """        el.gpsStartOverlay.style.display = 'block';
        el.gpsStopOverlay.style.display = 'none';
        el.gpsStatsOverlay.style.display = 'none';
        el.activityType.disabled = false;"""
content = content.replace(stop_logic_target, stop_logic_replacement)


# 3. Smart Units in JS
dropdown_target = """            item.addEventListener('click', () => {
              el.mealNameInput.value = f.name;
              el.customDropdown.style.display = 'none';
              calculateMealCals();
            });"""
dropdown_replacement = """            item.addEventListener('click', () => {
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
            });"""
content = content.replace(dropdown_target, dropdown_replacement)

# Make sure we remove the map variable duplicate definition if it was global
content = content.replace("let map, marker, pathLine;", "")


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Map UI redesigned and Smart Units added!")
