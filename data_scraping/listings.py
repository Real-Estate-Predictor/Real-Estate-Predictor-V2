from helperFunc.listingHelperFunc import listingUtils 
from helperFunc.pageHelperFunc import pageUtils
from helperFunc.helpers import process_string_list, create_file_if_not_exists
from playwright.sync_api import sync_playwright
import sys
from locationName.vancouver.vancouverWest import burnaby_part1


"""
****INPUTS****
"""

# neighbourhoods = burnaby_part1
# if none, scrapes the entire city
neighbourhoods = None

city = 'vancouver'
province = 'bc'
DoNotShowBrowser = True

startingPageNumber = 11
endingPageNumber = 25

csv_path = f'./{city}_real_estate_data.csv'

# for dev purposes, scrape only one listing
testSingleListing = False

showLogs = True

"""
PREPARE INPUTS
"""
# lower case and replace spaces with '-'
neighbourhoods = process_string_list(neighbourhoods) if neighbourhoods != None else None

create_file_if_not_exists(csv_path)

"""
ACTIVATE PLAYWRIGHT
"""
with sync_playwright() as p:

    # use proxy
    # https://playwright.dev/python/docs/network
    if len(sys.argv) > 1 and sys.argv[1]:
        browser = p.chromium.launch(
            headless=DoNotShowBrowser,
            slow_mo=500,
            proxy={"server": sys.argv[1]}
        )


    else:
        browser = p.chromium.launch(
            headless=DoNotShowBrowser, 
            slow_mo=500,
        )

    page = browser.new_page()

    # BLOCK IMAGE LOADING -> for playwright to load quicker
    # https://www.zenrows.com/blog/blocking-resources-in-playwright#block-by-resource-type
    page.route("**/*", lambda route: route.abort() 
	if route.request.resource_type == "image" 
	else route.continue_()
    )

    pageUtils().scrapPage(
        city=city, 
        province=province, 
        page=page,
        pageStart=startingPageNumber, 
        pageEnd=endingPageNumber, 
        neighborhoods=neighbourhoods,
        csv_file_path=csv_path, 
        TestSingleListing=testSingleListing,
        showLogs=showLogs
    )
