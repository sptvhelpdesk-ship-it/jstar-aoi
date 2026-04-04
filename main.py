import requests
import json
import sys
import os

# 🔗 ORIGINAL SOURCE
SOURCE_URL = "https://j-plus.free.nf/jtv/jstr.json"

# 🔥 YOUR CLOUDFLARE WORKER PROXY
PROXY_BASE = "https://tight-river-c898.ranatoufik66.workers.dev/?url="

# 🔗 FINAL FETCH URL
FINAL_URL = PROXY_BASE + SOURCE_URL

# 💾 OUTPUT FILE
OUTPUT_FILE = "channels.json"


def update_json():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "application/json",
        "Referer": "https://google.com",
        "Accept-Language": "en-US,en;q=0.9"
    }

    try:
        print(f"🔗 Fetching from proxy:")
        print(FINAL_URL)

        response = requests.get(
            FINAL_URL,
            headers=headers,
            timeout=60
        )

        # ❌ HTTP error check
        response.raise_for_status()

        print("✅ Download successful")

        # 🔍 Debug info
        content_type = response.headers.get("Content-Type", "")
        print("Content-Type:", content_type)

        # ❌ যদি JSON না হয়
        if "application/json" not in content_type:
            print("❌ Error: Response is NOT JSON")
            print("Preview:", response.text[:300])
            sys.exit(1)

        print("📦 Parsing JSON...")

        try:
            data = response.json()
        except json.JSONDecodeError:
            print("❌ JSON Decode Error")
            print("Preview:", response.text[:300])
            sys.exit(1)

        # 💾 Save JSON file
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
