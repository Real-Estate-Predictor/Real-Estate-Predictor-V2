from helperFunc.listingHelperFunc import listingUtils 
from helperFunc.pageHelperFunc import pageUtils
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from time import sleep
import sys

pageNum = 24
data_dic = {}

with sync_playwright() as p:

    # use proxy 
    # https://playwright.dev/python/docs/network
    if len(sys.argv) > 1 and sys.argv[1]:
        browser = p.chromium.launch(
            headless=False, 
            slow_mo=500,
            proxy={"server": sys.argv[1]}
        )
    else:
        browser = p.chromium.launch(
            headless=False, 
            slow_mo=500,
        )

    page = browser.new_page()

    # BLOCK IMAGE LOADING -> for playwright to load quicker
    # https://www.zenrows.com/blog/blocking-resources-in-playwright#block-by-resource-type
    page.route("**/*", lambda route: route.abort() 
	if route.request.resource_type == "image" 
	else route.continue_()
    )

    pageUtils().scrapPage('vancouver', 'bc', page, 1, 2, 'arbutus')
