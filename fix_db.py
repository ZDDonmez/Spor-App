import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_food_db = """
    const foodDatabase = [
      // Kahvaltılıklar & Süt Ürünleri
      { name: "Yumurta (Haşlanmış)", cal: 155, adet: 50, porsiyon: 100 }, 
      { name: "Yumurta (Sahanda)", cal: 210, adet: 50, porsiyon: 100 }, 
      { name: "Omlet (Sade)", cal: 154, porsiyon: 120 },
      { name: "Menemen", cal: 170, porsiyon: 200 }, 
      { name: "Beyaz Peynir (Tam Yağlı)", cal: 310, porsiyon: 60, adet: 30 }, // 1 dilim = 30g
      { name: "Beyaz Peynir (Light)", cal: 180, porsiyon: 60, adet: 30 },
      { name: "Kaşar Peyniri", cal: 350, porsiyon: 40, adet: 20 }, 
      { name: "Lor Peyniri", cal: 90, porsiyon: 50 }, 
      { name: "Tulum Peyniri", cal: 370, porsiyon: 40, adet: 20 },
      { name: "Siyah Zeytin", cal: 105, adet: 4, porsiyon: 40 }, // 1 zeytin ~4g
      { name: "Yeşil Zeytin", cal: 145, adet: 4, porsiyon: 40 }, 
      { name: "Tereyağı", cal: 717, adet: 10, porsiyon: 15 }, // 1 tatlı kaşığı ~10g
      { name: "Bal", cal: 304, adet: 15, porsiyon: 30 }, // 1 yemek kaşığı ~15g
      { name: "Reçel", cal: 278, adet: 15, porsiyon: 30 }, 
      { name: "Tahin", cal: 595, adet: 15, porsiyon: 30 }, 
      { name: "Pekmez", cal: 290, adet: 15, porsiyon: 30 },
      { name: "Ekmek (Beyaz)", cal: 265, adet: 30, porsiyon: 60 }, // 1 ince dilim ~30g
      { name: "Ekmek (Tam Buğday)", cal: 247, adet: 30, porsiyon: 60 }, 
      { name: "Ekmek (Çavdar)", cal: 259, adet: 30, porsiyon: 60 },
      { name: "Yulaf Ezmesi", cal: 389, adet: 10, porsiyon: 40 }, // 1 y.kaşığı ~10g
      { name: "Süt (Tam Yağlı)", cal: 61, porsiyon: 200 }, 
      { name: "Süt (Yarım Yağlı)", cal: 47, porsiyon: 200 },
      { name: "Süt (Laktozsuz)", cal: 43, porsiyon: 200 }, 
      { name: "Yoğurt (Tam Yağlı)", cal: 61, porsiyon: 200 }, 
      { name: "Süzme Yoğurt", cal: 112, porsiyon: 150 },
      { name: "Kefir", cal: 50, porsiyon: 200 }, 
      { name: "Sucuk", cal: 330, adet: 8, porsiyon: 50 }, // 1 ince dilim ~8g
      { name: "Sosis", cal: 300, adet: 30, porsiyon: 90 }, 
      { name: "Pastırma", cal: 250, adet: 10, porsiyon: 50 },
      { name: "Simit", cal: 275, adet: 100, porsiyon: 100 }, 
      { name: "Açma", cal: 350, adet: 120, porsiyon: 120 }, 
      { name: "Poğaça (Peynirli)", cal: 330, adet: 90, porsiyon: 90 },
      
      // Sebzeler & Meyveler
      { name: "Domates", cal: 18, adet: 110, porsiyon: 150 }, 
      { name: "Salatalık", cal: 15, adet: 120, porsiyon: 150 }, 
      { name: "Biber (Yeşil)", cal: 20, adet: 15, porsiyon: 100 },
      { name: "Soğan", cal: 40, adet: 100, porsiyon: 100 }, 
      { name: "Patates (Haşlama)", cal: 87, adet: 150, porsiyon: 200 }, 
      { name: "Patates Kızartması", cal: 312, porsiyon: 150 },
      { name: "Havuç", cal: 41, adet: 80, porsiyon: 100 }, 
      { name: "Kabak", cal: 16, adet: 150, porsiyon: 200 }, 
      { name: "Patlıcan", cal: 25, adet: 200, porsiyon: 200 }, 
      { name: "Brokoli", cal: 34, porsiyon: 150 },
      { name: "Karnabahar", cal: 25, porsiyon: 150 }, 
      { name: "Mantar", cal: 22, adet: 15, porsiyon: 150 }, 
      { name: "Elma", cal: 52, adet: 150, porsiyon: 150 }, 
      { name: "Muz", cal: 89, adet: 120, porsiyon: 120 },
      { name: "Portakal", cal: 47, adet: 130, porsiyon: 130 }, 
      { name: "Mandalina", cal: 53, adet: 80, porsiyon: 160 }, 
      { name: "Çilek", cal: 32, adet: 12, porsiyon: 150 }, 
      { name: "Karpuz", cal: 30, porsiyon: 200 }, // 1 porsiyon karpuz = 200g
      { name: "Kavun", cal: 34, porsiyon: 200 }, 
      { name: "Üzüm", cal: 69, porsiyon: 150 }, 
      { name: "Kiraz", cal: 50, adet: 6, porsiyon: 150 }, 
      { name: "Şeftali", cal: 39, adet: 150, porsiyon: 150 },
      
      // Ana Yemekler & Etler
      { name: "Pirinç Pilavı", cal: 130, porsiyon: 150 }, 
      { name: "Bulgur Pilavı", cal: 83, porsiyon: 150 }, 
      { name: "Makarna (Sade, Pişmiş)", cal: 158, porsiyon: 150 },
      { name: "Tavuk Göğsü (Izgara)", cal: 165, adet: 150, porsiyon: 150 }, 
      { name: "Tavuk But (Fırın)", cal: 210, adet: 120, porsiyon: 200 }, 
      { name: "Dana Eti (Az Yağlı)", cal: 250, porsiyon: 150 },
      { name: "Köfte (Izgara)", cal: 200, adet: 30, porsiyon: 120 }, // 1 köfte = 30g
      { name: "Kıyma (Dana)", cal: 332, porsiyon: 100 }, 
      { name: "Somon Balığı", cal: 208, porsiyon: 200 },
      { name: "Ton Balığı (Süzülmüş)", cal: 116, adet: 160, porsiyon: 160 }, // 1 kutu ton ~160g
      { name: "Mercimek Çorbası", cal: 56, porsiyon: 250 }, 
      { name: "Ezogelin Çorbası", cal: 54, porsiyon: 250 },
      { name: "Tarhana Çorbası", cal: 60, porsiyon: 250 }, 
      { name: "Tavuk Suyu Çorbası", cal: 45, porsiyon: 250 }, 
      { name: "Nohut Yemeği", cal: 164, porsiyon: 200 },
      { name: "Kuru Fasulye Yemeği", cal: 135, porsiyon: 200 }, 
      { name: "Zeytinyağlı Taze Fasulye", cal: 48, porsiyon: 200 }, 
      { name: "Ispanak Yemeği", cal: 45, porsiyon: 200 },
      { name: "Karnıyarık", cal: 130, adet: 200, porsiyon: 200 }, // 1 karnıyarık ~200g
      { name: "Mantı", cal: 170, porsiyon: 200 }, 
      { name: "Lahmacun", cal: 200, adet: 150, porsiyon: 150 }, // 1 adet lahmacun ~150g -> 300 kcal
      { name: "Pizza (Karışık)", cal: 266, adet: 100, porsiyon: 300 }, // 1 dilim ~100g
      { name: "Döner (Et)", cal: 250, porsiyon: 150 }, 
      { name: "Döner (Tavuk)", cal: 195, porsiyon: 150 },
      { name: "İskender Kebap", cal: 200, porsiyon: 400 }, 
      { name: "Adana Kebap", cal: 230, adet: 150, porsiyon: 150 }, 
      { name: "Tavuk Şiş", cal: 160, adet: 100, porsiyon: 200 }, // 1 şiş ~100g
      
      // Atıştırmalıklar & Kuruyemiş & Tatlı
      { name: "Ceviz", cal: 654, adet: 5, porsiyon: 30 }, // 1 tam ceviz içi ~5g
      { name: "Badem", cal: 579, adet: 1.5, porsiyon: 30 }, // 1 badem ~1.5g
      { name: "Fındık", cal: 628, adet: 1.5, porsiyon: 30 }, 
      { name: "Fıstık (Kavrulmuş)", cal: 585, adet: 1, porsiyon: 30 },
      { name: "Leblebi (Sarı)", cal: 380, porsiyon: 30 }, 
      { name: "Leblebi (Beyaz)", cal: 360, porsiyon: 30 }, 
      { name: "Kaju", cal: 553, adet: 2, porsiyon: 30 },
      { name: "Antep Fıstığı", cal: 560, adet: 1, porsiyon: 30 }, 
      { name: "Zeytinyağı", cal: 884, adet: 10, porsiyon: 15 }, // 1 yemek kaşığı ~10g
      { name: "Ayçiçek Yağı", cal: 884, adet: 10, porsiyon: 15 },
      { name: "Çikolata (Sütlü)", cal: 535, adet: 5, porsiyon: 40 }, // 1 kare ~5g
      { name: "Çikolata (Bitter)", cal: 546, adet: 5, porsiyon: 40 }, 
      { name: "Bisküvi (Sade)", cal: 433, adet: 6, porsiyon: 30 },
      { name: "Kek (Sade)", cal: 365, adet: 60, porsiyon: 100 }, 
      { name: "Dondurma", cal: 207, adet: 50, porsiyon: 100 }, // 1 top = 50g
      { name: "Baklava", cal: 420, adet: 40, porsiyon: 120 }, // 1 dilim ~40g -> 168 kcal
      { name: "Sütlaç", cal: 110, porsiyon: 250 }, 
      { name: "Kazandibi", cal: 130, porsiyon: 200 }, 
      { name: "Profiterol", cal: 280, porsiyon: 200 },
      { name: "Cips (Patates)", cal: 536, porsiyon: 50 }, 
      { name: "Patlamış Mısır (Sade)", cal: 387, porsiyon: 50 }, 
      { name: "Kraker (Tuzlu)", cal: 500, porsiyon: 40 },
      { name: "Protein Bar", cal: 350, adet: 50, porsiyon: 50 }, 
      { name: "Granola", cal: 470, porsiyon: 50 }, 
      { name: "Müsli", cal: 350, porsiyon: 50 },
      
      // İçecekler
      { name: "Kola", cal: 42, adet: 330, porsiyon: 250 }, // 1 kutu = 330ml
      { name: "Kola (Şekersiz)", cal: 0, adet: 330, porsiyon: 250 }, 
      { name: "Meyve Suyu", cal: 45, adet: 200, porsiyon: 200 },
      { name: "Ayran", cal: 37, adet: 200, porsiyon: 200 }, 
      { name: "Çay (Şekersiz)", cal: 0, porsiyon: 100 }, 
      { name: "Filtre Kahve (Sade)", cal: 1, porsiyon: 250 },
      { name: "Türk Kahvesi (Sade)", cal: 2, porsiyon: 70 }, 
      { name: "Latte", cal: 45, porsiyon: 350 }, 
      { name: "Mocha", cal: 80, porsiyon: 350 },
      { name: "Limonata", cal: 40, porsiyon: 250 }, 
      { name: "Bira", cal: 43, adet: 500, porsiyon: 500 }, 
      { name: "Şarap (Kırmızı)", cal: 85, porsiyon: 150 },
      { name: "Maden Suyu (Sade)", cal: 0, adet: 200, porsiyon: 200 }, 
      { name: "Maden Suyu (Meyveli)", cal: 25, adet: 200, porsiyon: 200 }, 
      { name: "Soğuk Çay (Ice Tea)", cal: 30, porsiyon: 250 }
    ];
"""

start_idx = content.find('const foodDatabase = [')
end_idx = content.find('];', start_idx) + 2

content = content[:start_idx] + new_food_db + content[end_idx:]

# Update calculation logic in JS
# We need to find the event listener for the meal form or `calculateMealCals`
calc_target = """      el.addMealForm.addEventListener('submit', (e) => {
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
          }"""

calc_replacement = """      el.addMealForm.addEventListener('submit', (e) => {
        e.preventDefault();
        let name = el.mealNameInput.value.trim();
        const amount = parseFloat(el.mealAmountInput.value.trim());
        const cal = parseInt(el.mealCaloriesInput.value, 10);
        
        if (name && cal > 0) {
          if (amount) {
            const unitText = el.mealUnitSelect.options[el.mealUnitSelect.selectedIndex].text;
            const unitSuffix = unitText === 'Gram / ml' ? 'g' : (unitText === 'Adet' ? ' adet' : ` ${unitText}`);
            name += ` (${amount}${unitSuffix})`;
          }"""

content = content.replace(calc_target, calc_replacement)

# Also need to replace the live calculation helper logic.
# I will use regex because it's safer
import re

live_calc_pattern = re.compile(
    r"const calculateMealCals = \(\) => \{.*?\};\n",
    re.DOTALL
)

live_calc_replacement = """const calculateMealCals = () => {
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
            
            const calculatedCal = Math.round((food.cal * totalWeight) / 100);
            el.mealCaloriesInput.value = calculatedCal;
            
            // Info text changes based on unit
            if (unitName === 'Gram / ml') {
              el.unitCalDisplay.innerHTML = `100 gramı <b>${food.cal}</b>`;
            } else if (unitName === 'Adet') {
              const perAdet = Math.round((food.cal * (food.adet || 100)) / 100);
              el.unitCalDisplay.innerHTML = `1 adeti (~${food.adet || 100}g) <b>${perAdet}</b>`;
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
"""

content = live_calc_pattern.sub(live_calc_replacement, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("DB and Calc logic updated!")
