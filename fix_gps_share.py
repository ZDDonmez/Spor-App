with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Change title
title_target = '<h2 class="section-title" style="margin: 0; font-size: 1.1rem; gap: 6px;">🌍 Canlı Rota Takibi</h2>'
title_replacement = '<h2 class="section-title" style="margin: 0; font-size: 1.1rem; gap: 6px;">🌍 Egzersiz Ekle</h2>'
content = content.replace(title_target, title_replacement)


# 2. Show Summary Modal on Stop
stop_target = """          state.walks.push({
            id: Date.now().toString(), name: currentActivityName, calories: currentWalkCal, distance: walkDistance.toFixed(2), time: new Date().toISOString()
          });
          saveState();
          updateUI();
          showToast(`${currentWalkCal} kcal yakıldı!`);
        }"""
stop_replacement = """          state.walks.push({
            id: Date.now().toString(), name: currentActivityName, calories: currentWalkCal, distance: walkDistance.toFixed(2), time: new Date().toISOString()
          });
          saveState();
          updateUI();
          showToast(`${currentWalkCal} kcal yakıldı!`);
          
          // Show share summary
          document.getElementById('summary-distance').textContent = walkDistance.toFixed(2);
          document.getElementById('summary-cal').textContent = currentWalkCal;
          document.getElementById('activity-summary-modal').classList.remove('hidden');
        }"""
content = content.replace(stop_target, stop_replacement)

# Ensure elements are defined in JS if they were not correctly handled. Let's see if close-summary-btn and share-summary-btn work.
# If they are not initialized in JS, they won't close. Let's check if close-summary-btn listener exists.
if "document.getElementById('close-summary-btn').addEventListener" not in content and "el.closeSummaryBtn" not in content:
    # We should add the listener at the end of setupEventListeners
    listener_target = """      el.startWalkBtn.addEventListener('click', () => {"""
    listener_replacement = """      document.getElementById('close-summary-btn').addEventListener('click', () => {
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
      
      el.startWalkBtn.addEventListener('click', () => {"""
    content = content.replace(listener_target, listener_replacement)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Share option and title changed!")
