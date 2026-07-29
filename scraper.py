import requests
import sys

print("=" * 80)
print("AGLOC SCRAPER STARTED")
print("=" * 80)

url = "https://www.agloc.org/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "en-US,en;q=0.9"
}

try:
    print(f"Fetching: {url}")

    response = requests.get(url, headers=headers, timeout=30)

    print(f"Status Code: {response.status_code}")
    print(f"Content Length: {len(response.text)}")

    print("=" * 80)
    print(response.text[:1000])
    print("=" * 80)

except Exception as e:
    print("ERROR:")
    print(e)
    sys.exit(1)

print("SCRAPER COMPLETED")
