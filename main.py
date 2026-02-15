import requests
import json

# আপনার দেওয়া মেইন লিঙ্ক
SOURCE_URL = "https://allinonereborn.online/jstrweb2/jstr.php"
# যে নামে ফাইল সেভ হবে
OUTPUT_FILE = "channels.json"

def update_json():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        print("Fetching data from source...")
        response = requests.get(SOURCE_URL, headers=headers, timeout=30)
        
        if response.status_code == 200:
            # ডেটা JSON হিসেবে রিড করা
            try:
                data = response.json()
                
                # হুবহু একই ফরম্যাটে সেভ করা (Same to same structure)
                with open(OUTPUT_FILE, "w", encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                
                print(f"Success! Data saved to {OUTPUT_FILE}")
                
            except json.JSONDecodeError:
                print("Error: Source did not return valid JSON.")
        else:
            print(f"Failed to fetch data. Status Code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    update_json()
