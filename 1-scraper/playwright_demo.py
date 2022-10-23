from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
url = 'https://www.rew.ca/'

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto(url)
    page.fill('input#listing_search_query','Vancouver')
    page.click('button[type=submit]')
    # page.is_visible('div.displaypanel-price')
    html = page.inner_html('div.col-xs-12.col-md-8')
    #print(html)
    page.click('a[href*="properties"]')
    page.is_visible('div.sectionblock')
    html1 = page.inner_html('div.sectionblock')
    print(html1)