from playwright.sync_api import sync_playwright
import time
import csv
import os

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    try:
        context = browser.new_context()
        page = context.new_page()
        page.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())
        page.goto("http://quotes.toscrape.com/js", wait_until="domcontentloaded")
        page.wait_for_selector(".quote")

        quote_blocks = page.locator(".quote").all()
        page_1 = []
        for block in quote_blocks:
            text = block.locator(".text").inner_text()
            author = block.locator(".author").inner_text()
            page_1.append([text, author])

        page.locator(".next a").click()
        page.wait_for_selector(".quote")
        time.sleep(1)

        quote_blocks = page.locator(".quote").all()
        page_2 = []
        for block in quote_blocks:
            text = block.locator(".text").inner_text()
            author = block.locator(".author").inner_text()
            page_2.append([text, author])

        os.makedirs("dynamic_scraper_data_output", exist_ok=True)
        all_data = page_1 + page_2

        with open("dynamic_scraper_data_output/quotes.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["quote", "author"])
            writer.writerows(all_data)
            print(f"Saved {len(all_data)} quotes")

    finally:
        browser.close()