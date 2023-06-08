import sys

from playwright.sync_api import sync_playwright

from .helperFunc.listingHelperFunc import ListingUtils 
from .helperFunc.pageHelperFunc import pageUtils
from .locationName.vancouver.vancouverWest import burnaby_part1


"""
****INPUTS****
"""

"""
ACTIVATE PLAYWRIGHT
"""
def activate_playwright_and_scrape(
    city, 
    province, 
    neighbourhoods, 
    csv_path, 
    starting_page_number, 
    ending_page_number, 
    test_single_listing, 
    show_logs, 
    do_not_show_browser, 
    proxy_server=None
):
    with sync_playwright() as p:
        # Use proxy if provided
        browser = p.chromium.launch(
            headless=do_not_show_browser,
            slow_mo=500,
            proxy={"server": proxy_server} if proxy_server else None
        )

        page = browser.new_page()

        # Block image loading for faster page loads
        page.route("**/*", lambda route: route.abort() 
            if route.request.resource_type == "image" 
            else route.continue_()
        )

        # Scrape the page
        pageUtils().scrapPage(
            city=city, 
            province=province, 
            page=page,
            pageStart=starting_page_number, 
            pageEnd=ending_page_number, 
            neighborhoods=neighbourhoods,
            csv_file_path=csv_path, 
            TestSingleListing=test_single_listing,
            showLogs=show_logs
        )

