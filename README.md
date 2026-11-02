# 02-dynamic-scraper-playwright — Month 2

Light, ethical scraper for JS-rendered content using Playwright. Handles dynamic tables and pagination that static scrapers can't.

Target: http://quotes.toscrape.com/js — open site that welcomes bots, JS quotes load after page load.

**Features:**
- Playwright with one context, one page reused
- Blocks images before goto for light load
- Waits for selector, not hard sleep
- Handles Next button pagination with 1 sec delay
- Try/finally close inside with

**Installation:**
pip install -r requirements.txt
playwright install

**Usage:**
python dynamic-scraper.py

**Output:**
`quotes.csv` — quotes from 2 pages

**Stack:** Python, Playwright

**License:** MIT
