import requests

url = "https://www.agloc.org/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "en-US,en;q=0.9"
}

try:
    response = requests.get(url, headers=headers, timeout=30)

    print("=" * 60)
    print("Status Code:", response.status_code)
    print("=" * 60)
    print(response.text[:1000])
    print("=" * 60)

except Exception as e:
    print(e)
