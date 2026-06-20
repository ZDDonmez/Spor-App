import json

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Expanded food database
new_food_db = """
    const foodDatabase = [
      // Kahvaltılıklar & Süt Ürünleri
      { name: "Yumurta (Haşlanmış)", cal: 155 }, { name: "Yumurta (Sahanda)", cal: 210 }, { name: "Omlet (Sade)", cal: 154 },
      { name: "Menemen", cal: 170 }, { name: "Beyaz Peynir (Tam Yağlı)", cal: 310 }, { name: "Beyaz Peynir (Light)", cal: 180 },
      { name: "Kaşar Peyniri", cal: 350 }, { name: "Lor Peyniri", cal: 90 }, { name: "Tulum Peyniri", cal: 370 },
      { name: "Siyah Zeytin", cal: 105 }, { name: "Yeşil Zeytin", cal: 145 }, { name: "Tereyağı", cal: 717 },
      { name: "Bal", cal: 304 }, { name: "Reçel", cal: 278 }, { name: "Tahin", cal: 595 }, { name: "Pekmez", cal: 290 },
      { name: "Ekmek (Beyaz)", cal: 265 }, { name: "Ekmek (Tam Buğday)", cal: 247 }, { name: "Ekmek (Çavdar)", cal: 259 },
      { name: "Yulaf Ezmesi", cal: 389 }, { name: "Süt (Tam Yağlı)", cal: 61 }, { name: "Süt (Yarım Yağlı)", cal: 47 },
      { name: "Süt (Laktozsuz)", cal: 43 }, { name: "Yoğurt (Tam Yağlı)", cal: 61 }, { name: "Süzme Yoğurt", cal: 112 },
      { name: "Kefir", cal: 50 }, { name: "Sucuk", cal: 330 }, { name: "Sosis", cal: 300 }, { name: "Pastırma", cal: 250 },
      { name: "Simit", cal: 275 }, { name: "Açma", cal: 350 }, { name: "Poğaça (Peynirli)", cal: 330 },
      // Sebzeler & Meyveler
      { name: "Domates", cal: 18 }, { name: "Salatalık", cal: 15 }, { name: "Biber (Yeşil)", cal: 20 },
      { name: "Soğan", cal: 40 }, { name: "Patates (Haşlama)", cal: 87 }, { name: "Patates Kızartması", cal: 312 },
      { name: "Havuç", cal: 41 }, { name: "Kabak", cal: 16 }, { name: "Patlıcan", cal: 25 }, { name: "Brokoli", cal: 34 },
      { name: "Karnabahar", cal: 25 }, { name: "Mantar", cal: 22 }, { name: "Elma", cal: 52 }, { name: "Muz", cal: 89 },
      { name: "Portakal", cal: 47 }, { name: "Mandalina", cal: 53 }, { name: "Çilek", cal: 32 }, { name: "Karpuz", cal: 30 },
      { name: "Kavun", cal: 34 }, { name: "Üzüm", cal: 69 }, { name: "Kiraz", cal: 50 }, { name: "Şeftali", cal: 39 },
      // Ana Yemekler & Etler
      { name: "Pirinç Pilavı", cal: 130 }, { name: "Bulgur Pilavı", cal: 83 }, { name: "Makarna (Sade, Pişmiş)", cal: 158 },
      { name: "Tavuk Göğsü (Izgara)", cal: 165 }, { name: "Tavuk But (Fırın)", cal: 210 }, { name: "Dana Eti (Az Yağlı)", cal: 250 },
      { name: "Köfte (Izgara)", cal: 200 }, { name: "Kıyma (Dana)", cal: 332 }, { name: "Somon Balığı", cal: 208 },
      { name: "Ton Balığı (Süzülmüş)", cal: 116 }, { name: "Mercimek Çorbası", cal: 56 }, { name: "Ezogelin Çorbası", cal: 54 },
      { name: "Tarhana Çorbası", cal: 60 }, { name: "Tavuk Suyu Çorbası", cal: 45 }, { name: "Nohut Yemeği", cal: 164 },
      { name: "Kuru Fasulye Yemeği", cal: 135 }, { name: "Zeytinyağlı Taze Fasulye", cal: 48 }, { name: "Ispanak Yemeği", cal: 45 },
      { name: "Karnıyarık", cal: 130 }, { name: "Mantı", cal: 170 }, { name: "Lahmacun (1 Adet)", cal: 200 }, # per 100g or 1 adet mapped, user will choose adet
      { name: "Pizza (Karışık)", cal: 266 }, { name: "Döner (Et)", cal: 250 }, { name: "Döner (Tavuk)", cal: 195 },
      { name: "İskender Kebap", cal: 200 }, { name: "Adana Kebap", cal: 230 }, { name: "Tavuk Şiş", cal: 160 },
      // Atıştırmalıklar & Kuruyemiş & Tatlı
      { name: "Ceviz", cal: 654 }, { name: "Badem", cal: 579 }, { name: "Fındık", cal: 628 }, { name: "Fıstık (Kavrulmuş)", cal: 585 },
      { name: "Leblebi (Sarı)", cal: 380 }, { name: "Leblebi (Beyaz)", cal: 360 }, { name: "Kaju", cal: 553 },
      { name: "Antep Fıstığı", cal: 560 }, { name: "Zeytinyağı", cal: 884 }, { name: "Ayçiçek Yağı", cal: 884 },
      { name: "Çikolata (Sütlü)", cal: 535 }, { name: "Çikolata (Bitter)", cal: 546 }, { name: "Bisküvi (Sade)", cal: 433 },
      { name: "Kek (Sade)", cal: 365 }, { name: "Dondurma", cal: 207 }, { name: "Baklava", cal: 420 },
      { name: "Sütlaç", cal: 110 }, { name: "Kazandibi", cal: 130 }, { name: "Profiterol", cal: 280 },
      { name: "Cips (Patates)", cal: 536 }, { name: "Patlamış Mısır (Sade)", cal: 387 }, { name: "Kraker (Tuzlu)", cal: 500 },
      { name: "Protein Bar", cal: 350 }, { name: "Granola", cal: 470 }, { name: "Müsli", cal: 350 },
      // İçecekler
      { name: "Kola", cal: 42 }, { name: "Kola (Şekersiz)", cal: 0 }, { name: "Meyve Suyu", cal: 45 },
      { name: "Ayran", cal: 37 }, { name: "Çay (Şekersiz)", cal: 0 }, { name: "Filtre Kahve (Sade)", cal: 1 },
      { name: "Türk Kahvesi (Sade)", cal: 2 }, { name: "Latte", cal: 45 }, { name: "Mocha", cal: 80 },
      { name: "Limonata", cal: 40 }, { name: "Bira", cal: 43 }, { name: "Şarap (Kırmızı)", cal: 85 },
      { name: "Maden Suyu (Sade)", cal: 0 }, { name: "Maden Suyu (Meyveli)", cal: 25 }, { name: "Soğuk Çay (Ice Tea)", cal: 30 }
    ];
"""

# Extract the existing style part
style_end = content.find('</style>')
head_part = content[:style_end]

css_additions = """
    /* Meal Categories */
    .meal-category-card { padding: 16px; margin-bottom: 16px; }
    .meal-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 1px solid var(--surface-border); padding-bottom: 8px; }
    .meal-header-right { display: flex; align-items: center; gap: 12px; }
    .category-cal { font-family: var(--font-heading); font-weight: 700; color: var(--accent-color); font-size: 1.1rem; }
    .add-meal-btn { width: 32px; height: 32px; padding: 0; border-radius: 50%; font-size: 1.2rem; display: flex; align-items: center; justify-content: center; }
"""

new_head = head_part + css_additions + "\n  </style>\n"

# Split content by </style> and <body>
body_start = content.find('<body>')
body_content = content[body_start:]

# Replace the Meal forms in the HTML
html_to_replace = """      <div class="glass-card">
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
      </div>"""

new_html_content = """
      <div class="glass-card meal-category-card">
        <div class="meal-header">
          <h2 class="section-title" style="margin-bottom: 0;">🍳 Kahvaltı</h2>
          <div class="meal-header-right">
            <span id="cal-breakfast" class="category-cal">0</span>
            <button class="add-meal-btn" data-category="breakfast">+</button>
          </div>
        </div>
        <ul id="list-breakfast" class="meal-list"></ul>
      </div>

      <div class="glass-card meal-category-card">
        <div class="meal-header">
          <h2 class="section-title" style="margin-bottom: 0;">🍲 Öğle Yemeği</h2>
          <div class="meal-header-right">
            <span id="cal-lunch" class="category-cal">0</span>
            <button class="add-meal-btn" data-category="lunch">+</button>
          </div>
        </div>
        <ul id="list-lunch" class="meal-list"></ul>
      </div>

      <div class="glass-card meal-category-card">
        <div class="meal-header">
          <h2 class="section-title" style="margin-bottom: 0;">🍽️ Akşam Yemeği</h2>
          <div class="meal-header-right">
            <span id="cal-dinner" class="category-cal">0</span>
            <button class="add-meal-btn" data-category="dinner">+</button>
          </div>
        </div>
        <ul id="list-dinner" class="meal-list"></ul>
      </div>

      <div class="glass-card meal-category-card" style="margin-bottom: 32px;">
        <div class="meal-header">
          <h2 class="section-title" style="margin-bottom: 0;">🍎 Ara Öğünler</h2>
          <div class="meal-header-right">
            <span id="cal-snack" class="category-cal">0</span>
            <button class="add-meal-btn" data-category="snack">+</button>
          </div>
        </div>
        <ul id="list-snack" class="meal-list"></ul>
      </div>"""

body_content = body_content.replace(html_to_replace, new_html_content)

# Add Meal Modal
modal_insertion_idx = body_content.find('  <!-- Onboarding Modal -->')

add_meal_modal = """
  <!-- Add Meal Modal -->
  <div id="add-meal-modal" class="overlay hidden" style="justify-content: flex-end; padding: 0; background: rgba(0,0,0,0.6);">
    <div class="glass-card" style="margin-bottom: 0; border-radius: 24px 24px 0 0; padding-bottom: 40px; animation: fadeSlideUp 0.3s ease;">
      <h2 class="section-title" id="add-meal-title" style="color: var(--accent-color);">Öğün Ekle</h2>
      <form id="add-meal-form">
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
                <option value="1">Adet</option>
              </select>
            </div>
          </div>
          <div class="input-group" style="flex: 1;">
            <label for="meal-calories">Kalori (kcal)</label>
            <input type="number" id="meal-calories" placeholder="350" required min="1">
          </div>
        </div>
        <div class="info-text" id="meal-calc-info" style="margin-top: -8px; margin-bottom: 16px; display: none;">
          100 gramı / 1 adeti <span id="unit-cal-display" style="color: var(--accent-color); font-weight: 600;">0</span> kcal.
        </div>
        <button type="submit" style="margin-bottom: 12px;">Ekle</button>
        <button type="button" id="close-meal-modal" class="secondary-btn">İptal</button>
      </form>
    </div>
  </div>
"""

body_content = body_content[:modal_insertion_idx] + add_meal_modal + body_content[modal_insertion_idx:]

# Replace JS database
start_idx = body_content.find('const foodDatabase = [')
end_idx = body_content.find('];', start_idx) + 2

body_content = body_content[:start_idx] + new_food_db + body_content[end_idx:]

# Update elements
el_target = """      addMealForm: document.getElementById('add-meal-form'),
      mealNameInput: document.getElementById('meal-name'),
      mealAmountInput: document.getElementById('meal-amount'),
      mealUnitSelect: document.getElementById('meal-unit'),
      mealCaloriesInput: document.getElementById('meal-calories'),
      foodDbList: document.getElementById('food-db'),
      mealCalcInfo: document.getElementById('meal-calc-info'),
      unitCalDisplay: document.getElementById('unit-cal-display'),
      mealList: document.getElementById('meal-list'),
      emptyMeals: document.getElementById('empty-meals'),"""

el_replacement = """      addMealModal: document.getElementById('add-meal-modal'),
      addMealTitle: document.getElementById('add-meal-title'),
      closeMealModalBtn: document.getElementById('close-meal-modal'),
      addMealForm: document.getElementById('add-meal-form'),
      mealNameInput: document.getElementById('meal-name'),
      mealAmountInput: document.getElementById('meal-amount'),
      mealUnitSelect: document.getElementById('meal-unit'),
      mealCaloriesInput: document.getElementById('meal-calories'),
      foodDbList: document.getElementById('food-db'),
      mealCalcInfo: document.getElementById('meal-calc-info'),
      unitCalDisplay: document.getElementById('unit-cal-display'),
      
      lists: {
        breakfast: document.getElementById('list-breakfast'),
        lunch: document.getElementById('list-lunch'),
        dinner: document.getElementById('list-dinner'),
        snack: document.getElementById('list-snack')
      },
      cals: {
        breakfast: document.getElementById('cal-breakfast'),
        lunch: document.getElementById('cal-lunch'),
        dinner: document.getElementById('cal-dinner'),
        snack: document.getElementById('cal-snack')
      },"""
body_content = body_content.replace(el_target, el_replacement)

# Update `updateUI` logic
ui_target = """      el.mealList.innerHTML = '';
      if (state.meals.length === 0) {
        el.emptyMeals.style.display = 'block';
      } else {
        el.emptyMeals.style.display = 'none';
        state.meals.forEach(meal => {
          const li = document.createElement('li');
          li.className = 'meal-item';
          li.innerHTML = `
            <div class="meal-info">
              <div class="meal-name">${escapeHTML(meal.name)}</div>
              <div class="meal-cal">${meal.calories} kcal</div>
            </div>
            <button class="delete-btn" onclick="deleteMeal('${meal.id}')">&times;</button>
          `;
          el.mealList.appendChild(li);
        });
      }"""

ui_replacement = """      // Clear lists
      Object.values(el.lists).forEach(list => list.innerHTML = '');
      let categoryTotals = { breakfast: 0, lunch: 0, dinner: 0, snack: 0 };

      state.meals.forEach(meal => {
        const cat = meal.category || 'snack'; // fallback for old meals
        categoryTotals[cat] += meal.calories;
        
        const li = document.createElement('li');
        li.className = 'meal-item';
        li.innerHTML = `
          <div class="meal-info">
            <div class="meal-name">${escapeHTML(meal.name)}</div>
            <div class="meal-cal">${meal.calories} kcal</div>
          </div>
          <button class="delete-btn" onclick="deleteMeal('${meal.id}')">&times;</button>
        `;
        if(el.lists[cat]) el.lists[cat].appendChild(li);
      });

      // Update subtotals and empty states
      Object.keys(categoryTotals).forEach(cat => {
        el.cals[cat].textContent = categoryTotals[cat];
        if (el.lists[cat].innerHTML === '') {
          el.lists[cat].innerHTML = '<li class="empty-state" style="padding: 10px;">Henüz eklenmedi.</li>';
        }
      });"""
body_content = body_content.replace(ui_target, ui_replacement)

# Update `setupEventListeners`
ev_target = """      el.addMealForm.addEventListener('submit', (e) => {
        e.preventDefault();
        let name = el.mealNameInput.value.trim();
        const amount = el.mealAmountInput.value.trim();
        const cal = parseInt(el.mealCaloriesInput.value, 10);
        
        if (name && cal > 0) {
          if (amount) {
            const unitMultiplier = parseFloat(el.mealUnitSelect.value);
            const unitText = el.mealUnitSelect.options[el.mealUnitSelect.selectedIndex].text;
            const unitSuffix = unitMultiplier === 1 ? 'g' : ` ${unitText}`;
            name += ` (${amount}${unitSuffix})`;
          }
          state.meals.unshift({
            id: Date.now().toString(), name, calories: cal, time: new Date().toISOString()
          });
          state.consumedCalories += cal;
          
          pulseRing();
          el.mealNameInput.value = ''; el.mealAmountInput.value = ''; el.mealCaloriesInput.value = '';
          el.mealCalcInfo.style.display = 'none';
          saveState();
          showToast('Öğün eklendi');
        }
      });"""

ev_replacement = """      let currentMealCategory = 'snack';
      
      const catNames = { breakfast: 'Kahvaltı', lunch: 'Öğle Yemeği', dinner: 'Akşam Yemeği', snack: 'Ara Öğün' };

      document.querySelectorAll('.add-meal-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          currentMealCategory = btn.getAttribute('data-category');
          el.addMealTitle.textContent = catNames[currentMealCategory] + ' Ekle';
          el.addMealModal.classList.remove('hidden');
        });
      });

      el.closeMealModalBtn.addEventListener('click', () => {
        el.addMealModal.classList.add('hidden');
      });

      el.addMealForm.addEventListener('submit', (e) => {
        e.preventDefault();
        let name = el.mealNameInput.value.trim();
        const amount = el.mealAmountInput.value.trim();
        const cal = parseInt(el.mealCaloriesInput.value, 10);
        
        if (name && cal > 0) {
          if (amount) {
            const unitMultiplier = parseFloat(el.mealUnitSelect.value);
            const unitText = el.mealUnitSelect.options[el.mealUnitSelect.selectedIndex].text;
            const unitSuffix = unitMultiplier === 1 ? (el.mealUnitSelect.options[el.mealUnitSelect.selectedIndex].text === 'Adet' ? ' adet' : 'g') : ` ${unitText}`;
            name += ` (${amount}${unitSuffix})`;
          }
          state.meals.push({ // push instead of unshift to keep chronological or keep unshift. Unshift is better for "latest top". Let's keep unshift.
            id: Date.now().toString(), 
            name, 
            calories: cal, 
            category: currentMealCategory,
            time: new Date().toISOString()
          });
          state.consumedCalories += cal;
          
          pulseRing();
          el.mealNameInput.value = ''; el.mealAmountInput.value = ''; el.mealCaloriesInput.value = '';
          el.mealCalcInfo.style.display = 'none';
          el.addMealModal.classList.add('hidden');
          saveState();
          showToast('Öğün eklendi');
        }
      });"""
body_content = body_content.replace(ev_target, ev_replacement)

# Finally write out
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_head + body_content)

print("V4 Updated successfully.")
