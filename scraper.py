from playwright.sync_api import sync_playwright

URL = "https://www.agloc.org/"

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=True
    )

    page = browser.new_page(
        viewport={"width": 1600, "height": 900}
    )

    print("Opening website...")

    page.goto(URL, wait_until="networkidle", timeout=60000)

    page.screenshot(
        path="agloc.png",
        full_page=True
    )

    print("Screenshot saved.")

    browser.close()
