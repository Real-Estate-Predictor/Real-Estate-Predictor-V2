from bs4 import BeautifulSoup
from helperFunc.listingHelperFunc import listingUtils 
from time import sleep
import random

class pageUtils:
    def isNextPageAvailable(self, html_source: str) -> bool:
        soup = BeautifulSoup(html_source, 'html.parser')
        button = soup.find('li', class_='paginator-next_page paginator-control')
        return button is not None
    
    def scrapPage(self,  city, province, page, pageStart=1, pageEnd=None, neighborhoods=None, csv_file_path='real_estate_data.csv',  TestSingleListing=False, showLogs=True):
        pageNum = pageStart

        for neighborhood in neighborhoods:
            
            neighborhood = '' if neighborhood is None else neighborhood + '-'
            
            try:
                while True:
                    url = f'https://www.rew.ca/properties/areas/{neighborhood}{city}-{province}/page/{pageNum}'
                    if showLogs: print(f"scraping url: {url}")
                    
                    page.goto(url)

                    listing = page.query_selector_all('.displaypanel')

                    # iterate through listings
                    for i in range(len(listing)):

                        # for testing purposes only, will stop after scraping one listing
                        if TestSingleListing and i == 1: break

                        currListing = listing[i]

                        # open listing in new tab
                        with page.context.expect_page() as tab:
                            try:

                                currListing.click(modifiers=['Meta'])
                                new_tab = tab.value
                                new_tab.wait_for_load_state("networkidle") 
                                new_tab.wait_for_load_state("domcontentloaded")

                                html1 = new_tab.inner_html('div.col-xs-12.col-md-8')

                                # extract listing info into dictionary
                                dic_data = listingUtils().get_info(html1)
                                # if showLogs: print(dic_data)
                                # sleep random time to prevent detection
                                sleep(random.randint(2, 5))

                                # write to given csv
                                listingUtils().write_to_csv(dic_data, csv_file_path)
                                
                                # print(dic_data)
                                if showLogs: print(f"Scraped data for address: {dic_data['address']}")

                                new_tab.close()
                            except Exception as e:
                                if showLogs: print('error occur')
                                # print(e)
                                new_tab.close()

                    # check if next page exist or not
                    # c = page.inner_html('li.paginator-next_page.paginator-control')
                    if pageEnd is not None and pageEnd == pageNum: break
                    if not pageUtils().isNextPageAvailable(page.content()): break
                    if TestSingleListing: break
                    
                    pageNum+=1

                sleep(random.randint(5, 7))
            except Exception as e:
                print("page could not be retrieved at url:{url}")
                print(e)
