import requests

url = "https://www.agloc.org/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

print("=" * 80)
print("AGLOC SCRAPER STARTED")
print("=" * 80)

response = requests.get(url, headers=headers, timeout=30)

print("Status Code:", response.status_code)
print("Content Length:", len(response.text))

with open("output.html", "w", encoding="utf-8") as f:
    f.write(response.text)

print("output.html saved successfully")
print("=" * 80)
print("SCRAPER COMPLETED")
