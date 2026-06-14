import json
import requests
from bs4 import BeautifulSoup

URL = "https://www.365scores.com/he/football/league/fifa-world-cup-5930"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def fetch_world_cup_data():
    print("🔄 סורק תוצאות מעודכנות מ-365Scores...")
    try:
        response = requests.get(URL, headers=HEADERS)
        if response.status_code != 200:
            print("⚠️ שגיאה בגישה לאתר.")
            return
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        with open('data.json', 'r', encoding='utf-8') as f:
            current_matches = json.load(f)
            
        # כאן הבוט מעדכן אוטומטית את המשחקים לפי מה שקורה באתר של 365Scores
        # (כרגע זה מעדכן משחק לדוגמה כדי לוודא שהמערכת עובדת)
        for match in current_matches:
            if match['id'] == 2: 
                match['status'] = 'LIVE'
                match['homeScore'] = 1
                match['awayScore'] = 2
                match['broadcast'] = 'כאן 11'
                
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(current_matches, f, ensure_ascii=False, indent=2)
        print("✅ קובץ data.json עודכן בהצלחה בענן!")
        
    except Exception as e:
        print(f"❌ שגיאה: {e}")

if __name__ == "__main__":
    fetch_world_cup_data()
