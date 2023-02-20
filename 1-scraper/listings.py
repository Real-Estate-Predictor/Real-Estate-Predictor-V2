"""
arguments: 
city, province, pageStart, pageEnd

How to run example: 
python3 listings.py vancouver bc 1 2
"""


from helperFunc.listingHelperFunc import listingUtils 
from helperFunc.pageHelperFunc import pageUtils
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from locationName.vancouver.vancouverWest import vancouver_west_neighbourhoods
import sys

city = sys.argv[1]
province = sys.argv[2]
pageStart = sys.argv[3]
pageEnd = sys.argv[4]
neighborhoods = vancouver_west_neighbourhoods 


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

    pageUtils().scrapPage(city, province, page,pageStart, pageEnd)
