from helperFunc import Utils 
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from time import sleep
import sys

url = 'https://www.rew.ca/properties/areas/vancouver-bc'
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

    page.goto(url)

    # list of all elements taht contain .displaypanel 
    # listings = page.query_selector_all('.displaypanel')

    # click on the first display panel
    # firstListing = listings[0]
    # firstListing.click()
    # page.wait_for_load_state()

    # sleep(3)
    # html1 = page.inner_html('div.col-xs-12.col-md-8')
    # test = Utils().get_info(html1)
    # print(test)
    # # go back
    # page.goto(url)
    # page.wait_for_load_state()
    # sleep(3)

    # click on the second one
    
    listing = page.query_selector_all('.displaypanel')
    for i in range(len(listing)):
        if i == 2:
            break
        # listing = page.query_selector_all('.displaypanel')
        currListing = listing[i]
        
        with page.context.expect_page() as tab:
            currListing.click(modifiers=['Meta'])
            #page.click("#tabButton")
            new_tab = tab.value
            new_tab.wait_for_load_state()
            html1 = new_tab.inner_html('div.col-xs-12.col-md-8')
            
            dic_data = Utils().get_info(html1)
            Utils().write_to_csv(dic_data)
            print(dic_data.keys())
            new_tab.close()
        # currListing.click()
        # newPage.wait_for_load_state()
        
       
        
        # page.goto(url)
    

# const browser = await playwright["chromium"].launch({headless : false});
# const page = await browser.newPage();
# await page.goto('https://www.facebook.com/');
# var pagePromise = page.context().waitForEvent('page', p => p.url() =='https://www.messenger.com/');
# await page.click('text=Messenger', { modifiers: ['Meta']});
# const newPage = await pagePromise;
# await newPage.bringToFront();
# await browser.close();
    # # go back
    # page.goto(url)

    # # do not close too soon
    # sleep(10)