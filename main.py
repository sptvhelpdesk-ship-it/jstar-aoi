import requests
import json
import sys
import os

# আপনার লিঙ্ক
SOURCE_URL = "https://allinonereborn.online/jstrweb2/jstr.php"
OUTPUT_FILE = "channels.json"

def update_json():
    # ব্রাউজারের মতো হেডার দেওয়া হলো যাতে ব্লক না করে
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Referer": "https://allinonereborn.online/",
        "Accept-Language": "en-US,en;q=0.9"
    }

    try:
        print(f"Connecting to {SOURCE_URL}...")
        response = requests.get(SOURCE_URL, headers=headers, timeout=60)
        
        # যদি লিঙ্ক কাজ না করে (যেমন 403, 404, 500) তবে সরাসরি এরর দেবে
        response.raise_for_status()
        
        print("Download successful. Parsing JSON...")
        
        try:
            data = response.json()
        except json.JSONDecodeError:
            print("Error: The response is not valid JSON.")
            print("Response text preview:", response.text[:200]) # কী রেসপন্স এসেছে তা দেখাবে
            sys.exit(1) # ফেইল করাবে

        # ফাইল সেভ করা
        with open(OUTPUT_FILE, "w", encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"Success! Data saved to {OUTPUT_FILE}")
        
        # ফাইলটি সত্যি তৈরি হয়েছে কিনা চেক করা
        if os.path.exists(OUTPUT_FILE):
            print(f"Verification: {OUTPUT_FILE} exists.")
        else:
            print(f"Error: {OUTPUT_FILE} was not created.")
            sys.exit(1)

    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}")
        sys.exit(1) # GitHub Action লাল দেখাবে
    except Exception as e:
        print(f"General Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    update_json()
