from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from time import sleep
url = 'https://www.rew.ca/properties/areas/vancouver-bc'

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto(url)

    # list of all elements taht contain .displaypanel 
    listings = page.query_selector_all('.displaypanel')

    # click on the first display panel
    firstListing = listings[0]
    firstListing.click()
    page.wait_for_load_state()

    sleep(3)

    # go back
    page.goto(url)
    page.wait_for_load_state()
    sleep(3)

    # click on the second one
    secondListing = page.query_selector_all('.displaypanel')[1]
    page.wait_for_load_state()
    secondListing.click()

    # go back
    page.goto(url)

    # do not close too soon
    sleep(10)