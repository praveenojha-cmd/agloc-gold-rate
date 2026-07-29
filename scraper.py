import requests

url = "https://www.agloc.org/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

print("===== START =====")

response = requests.get(url, headers=headers, timeout=30)

print("Status:", response.status_code)

with open("output.html", "w", encoding="utf-8") as f:
    f.write(response.text)

print("Saved output.html")
print("===== END =====")
