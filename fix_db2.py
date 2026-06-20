import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the amount input to allow decimals
input_target = '<input type="number" id="meal-amount" placeholder="100" min="1" style="flex: 1;">'
input_replacement = '<input type="number" id="meal-amount" placeholder="Örn: 1 veya 0.5" min="0.1" step="0.1" style="flex: 1;">'
content = content.replace(input_target, input_replacement)

# 2. Add 'Dilim' to the unit select
select_target = """                <option value="150">Porsiyon</option>
                <option value="1">Adet</option>
              </select>"""
select_replacement = """                <option value="150">Porsiyon</option>
                <option value="1">Adet</option>
                <option value="1">Dilim</option>
              </select>"""
content = content.replace(select_target, select_replacement)

# 3. Update calculateMealCals logic to handle Dilim
calc_target = """            else if (unitName === 'Adet') totalWeight = amount * (food.adet || 100);
            
            const calculatedCal = Math.round((food.cal * totalWeight) / 100);"""
calc_replacement = """            else if (unitName === 'Adet') totalWeight = amount * (food.adet || 100);
            else if (unitName === 'Dilim') totalWeight = amount * (food.dilim || food.adet || 100);
            
            const calculatedCal = Math.round((food.cal * totalWeight) / 100);"""
content = content.replace(calc_target, calc_replacement)

info_target = """            } else if (unitName === 'Adet') {
              const perAdet = Math.round((food.cal * (food.adet || 100)) / 100);
              el.unitCalDisplay.innerHTML = `1 adeti (~${food.adet || 100}g) <b>${perAdet}</b>`;"""
info_replacement = """            } else if (unitName === 'Adet') {
              const perAdet = Math.round((food.cal * (food.adet || 100)) / 100);
              el.unitCalDisplay.innerHTML = `1 adeti (~${food.adet || 100}g) <b>${perAdet}</b>`;
            } else if (unitName === 'Dilim') {
              const perDilim = Math.round((food.cal * (food.dilim || food.adet || 100)) / 100);
              el.unitCalDisplay.innerHTML = `1 dilimi (~${food.dilim || food.adet || 100}g) <b>${perDilim}</b>`;"""
content = content.replace(info_target, info_replacement)

# 4. Expand food database
start_idx = content.find('const foodDatabase = [')
end_idx = content.find('];', start_idx) + 2

# We will just rewrite the foodDatabase entirely to add the new ones cleanly.
new_food_db = """
    const foodDatabase = [
      // Kahvaltılıklar & Süt Ürünleri
      { name: "Yumurta (Haşlanmış)", cal: 155, adet: 50, porsiyon: 100 }, 
      { name: "Yumurta (Sahanda)", cal: 210, adet: 50, porsiyon: 100 }, 
      { name: "Omlet (Sade)", cal: 154, porsiyon: 120 },
      { name: "Menemen", cal: 170, porsiyon: 200 }, 
      { name: "Beyaz Peynir (Tam Yağlı)", cal: 310, porsiyon: 60, adet: 30, dilim: 30 }, 
      { name: "Beyaz Peynir (Light)", cal: 180, porsiyon: 60, adet: 30, dilim: 30 },
      { name: "Kaşar Peyniri", cal: 350, porsiyon: 40, adet: 20, dilim: 20 }, 
      { name: "Lor Peyniri", cal: 90, porsiyon: 50 }, 
      { name: "Tulum Peyniri", cal: 370, porsiyon: 40, adet: 20, dilim: 20 },
      { name: "Siyah Zeytin", cal: 105, adet: 4, porsiyon: 40 }, 
      { name: "Yeşil Zeytin", cal: 145, adet: 4, porsiyon: 40 }, 
      { name: "Tereyağı", cal: 717, adet: 10, porsiyon: 15 }, 
      { name: "Bal", cal: 304, adet: 15, porsiyon: 30 }, 
      { name: "Reçel", cal: 278, adet: 15, porsiyon: 30 }, 
      { name: "Tahin", cal: 595, adet: 15, porsiyon: 30 }, 
      { name: "Pekmez", cal: 290, adet: 15, porsiyon: 30 },
      { name: "Ekmek (Beyaz)", cal: 265, adet: 30, porsiyon: 60, dilim: 30 }, 
      { name: "Ekmek (Tam Buğday)", cal: 247, adet: 30, porsiyon: 60, dilim: 30 }, 
      { name: "Ekmek (Çavdar)", cal: 259, adet: 30, porsiyon: 60, dilim: 30 },
      { name: "Yulaf Ezmesi", cal: 389, adet: 10, porsiyon: 40 }, 
      { name: "Süt (Tam Yağlı)", cal: 61, porsiyon: 200 }, 
      { name: "Süt (Yarım Yağlı)", cal: 47, porsiyon: 200 },
      { name: "Süt (Laktozsuz)", cal: 43, porsiyon: 200 }, 
      { name: "Yoğurt (Tam Yağlı)", cal: 61, porsiyon: 200 }, 
      { name: "Süzme Yoğurt", cal: 112, porsiyon: 150 },
      { name: "Kefir", cal: 50, porsiyon: 200 }, 
      { name: "Sucuk", cal: 330, adet: 8, porsiyon: 50, dilim: 8 }, 
      { name: "Sosis", cal: 300, adet: 30, porsiyon: 90 }, 
      { name: "Pastırma", cal: 250, adet: 10, porsiyon: 50, dilim: 10 },
      { name: "Simit", cal: 275, adet: 100, porsiyon: 100 }, 
      { name: "Açma", cal: 350, adet: 120, porsiyon: 120 }, 
      { name: "Poğaça (Sade)", cal: 340, adet: 90, porsiyon: 90 },
      { name: "Poğaça (Peynirli)", cal: 330, adet: 90, porsiyon: 90 },
      { name: "Poğaça (Zeytinli)", cal: 350, adet: 90, porsiyon: 90 },
      { name: "Poğaça (Sosisli)", cal: 365, adet: 90, porsiyon: 90 },
      { name: "Poğaça (Kaşarlı)", cal: 360, adet: 90, porsiyon: 90 },
      { name: "Poğaça (Patatesli)", cal: 320, adet: 90, porsiyon: 90 },
      
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
      { name: "Karpuz", cal: 30, dilim: 200, porsiyon: 200 }, 
      { name: "Kavun", cal: 34, dilim: 200, porsiyon: 200 }, 
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
      { name: "Köfte (Izgara)", cal: 200, adet: 30, porsiyon: 120 }, 
      { name: "Kıyma (Dana)", cal: 332, porsiyon: 100 }, 
      { name: "Somon Balığı", cal: 208, porsiyon: 200 },
      { name: "Ton Balığı (Süzülmüş)", cal: 116, adet: 160, porsiyon: 160 }, 
      { name: "Mercimek Çorbası", cal: 56, porsiyon: 250 }, 
      { name: "Ezogelin Çorbası", cal: 54, porsiyon: 250 },
      { name: "Tarhana Çorbası", cal: 60, porsiyon: 250 }, 
      { name: "Tavuk Suyu Çorbası", cal: 45, porsiyon: 250 }, 
      { name: "Nohut Yemeği", cal: 164, porsiyon: 200 },
      { name: "Kuru Fasulye Yemeği", cal: 135, porsiyon: 200 }, 
      { name: "Zeytinyağlı Taze Fasulye", cal: 48, porsiyon: 200 }, 
      { name: "Ispanak Yemeği", cal: 45, porsiyon: 200 },
      { name: "Karnıyarık", cal: 130, adet: 200, porsiyon: 200 }, 
      { name: "Mantı", cal: 170, porsiyon: 200 }, 
      { name: "Lahmacun", cal: 200, adet: 150, porsiyon: 150 }, 
      
      // Pizzalar
      { name: "Pizza (Küçük Boy)", cal: 260, dilim: 70, adet: 420, porsiyon: 210 }, 
      { name: "Pizza (Orta Boy)", cal: 260, dilim: 100, adet: 800, porsiyon: 300 }, 
      { name: "Pizza (Büyük Boy)", cal: 260, dilim: 130, adet: 1040, porsiyon: 390 }, 
      { name: "Pizza (İnce Hamur İtalyan)", cal: 220, dilim: 80, porsiyon: 240 },
      
      // Döner & Kebap
      { name: "Döner (Et)", cal: 250, porsiyon: 150 }, 
      { name: "Döner (Tavuk)", cal: 195, porsiyon: 150 },
      { name: "İskender Kebap", cal: 200, porsiyon: 400 }, 
      { name: "Adana Kebap", cal: 230, adet: 150, porsiyon: 150 }, 
      { name: "Tavuk Şiş", cal: 160, adet: 100, porsiyon: 200 }, 
      
      // Atıştırmalıklar & Kuruyemiş & Tatlı
      { name: "Ceviz", cal: 654, adet: 5, porsiyon: 30 }, 
      { name: "Badem", cal: 579, adet: 1.5, porsiyon: 30 }, 
      { name: "Fındık", cal: 628, adet: 1.5, porsiyon: 30 }, 
      { name: "Fıstık (Kavrulmuş)", cal: 585, adet: 1, porsiyon: 30 },
      { name: "Leblebi (Sarı)", cal: 380, porsiyon: 30 }, 
      { name: "Leblebi (Beyaz)", cal: 360, porsiyon: 30 }, 
      { name: "Kaju", cal: 553, adet: 2, porsiyon: 30 },
      { name: "Antep Fıstığı", cal: 560, adet: 1, porsiyon: 30 }, 
      { name: "Zeytinyağı", cal: 884, adet: 10, porsiyon: 15 }, 
      { name: "Ayçiçek Yağı", cal: 884, adet: 10, porsiyon: 15 },
      { name: "Çikolata (Sütlü)", cal: 535, adet: 5, porsiyon: 40 }, 
      { name: "Çikolata (Bitter)", cal: 546, adet: 5, porsiyon: 40 }, 
      { name: "Bisküvi (Sade)", cal: 433, adet: 6, porsiyon: 30 },
      { name: "Kek (Sade)", cal: 365, adet: 60, dilim: 60, porsiyon: 100 }, 
      { name: "Dondurma", cal: 207, adet: 50, porsiyon: 100 }, 
      { name: "Baklava", cal: 420, adet: 40, dilim: 40, porsiyon: 120 }, 
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
      { name: "Kola", cal: 42, adet: 330, porsiyon: 250 }, 
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

content = content[:start_idx] + new_food_db + content[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("DB and fractional input updated!")
