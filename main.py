import requests
import json
import sys
import os

# 🔗 SOURCE LINK
SOURCE_URL = "https://j-plus.free.nf/jtv/jstr.json"

# 💾 OUTPUT FILE
OUTPUT_FILE = "channels.json"


def update_json():
    # ✅ Proper headers (anti-bot bypass)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "application/json",
        "Referer": "https://google.com",
        "Accept-Language": "en-US,en;q=0.9"
    }

    try:
        print(f"🔗 Connecting to {SOURCE_URL}...")
        
        response = requests.get(
            SOURCE_URL,
            headers=headers,
            timeout=60
        )

        # ❌ HTTP error check
        response.raise_for_status()

        print("✅ Download successful")

        # 🔍 Check response type
        content_type = response.headers.get("Content-Type", "")

        if "application/json" not in content_type:
            print("❌ Error: Response is NOT JSON")
            print("Content-Type:", content_type)
            print("Preview:", response.text[:200])
            sys.exit(1)

        print("📦 Parsing JSON...")

        try:
            data = response.json()
        except json.JSONDecodeError:
            print("❌ JSON Decode Error")
            print("Preview:", response.text[:200])
            sys.exit(1)

        # 💾 Save file
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"✅ Success! Data saved to {OUTPUT_FILE}")

        # 🔍 Verify file exists
        if os.path.exists(OUTPUT_FILE):
            print(f"✔️ Verification: {OUTPUT_FILE} exists")
        else:
            print(f"❌ Error: {OUTPUT_FILE} not found")
            sys.exit(1)

    except requests.exceptions.RequestException as e:
        print(f"❌ Network Error: {e}")
        sys.exit(1)

    except Exception as e:
        print(f"❌ General Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    update_json()
