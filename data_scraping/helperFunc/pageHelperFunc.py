from bs4 import BeautifulSoup

from time import sleep
import random

from data_scraping.helperFunc.columnNames import column_names
from data_scraping.helperFunc.utils import write_to_csv
from .listingHelperFunc import ListingUtils, exception_handler 


class pageUtils:
    # def isNextPageAvailable(self, html_source: str) -> bool:
    #     soup = BeautifulSoup(html_source, 'html.parser')
    #     button = soup.find('li', class_='paginator-next_page paginator-control')
    #     return button is not None
    def isNextPageAvailable(self, source_code: str) -> bool:
        soup = BeautifulSoup(source_code, 'html.parser')
        return False if soup.find('a') == None else True
    
    def open_new_tab(self, page, curListing):
        
        dic_data = {}
        # open listing in new tab
        with page.context.expect_page() as tab:
            try:
                # sleep random time to prevent detection
                sleep(random.randint(3, 4))

                curListing.click(modifiers=['Meta'])
                new_tab = tab.value
                new_tab.wait_for_load_state("networkidle") 
                new_tab.wait_for_load_state("domcontentloaded")
                sleep(random.randint(3, 5))

                html1 = new_tab.inner_html('div.col-xs-12.col-md-8')

                # extract listing info into dictionary
                dic_data = ListingUtils().get_info(html1)
                # if showLogs: print(dic_data)
                
                new_tab.close()
                return dic_data
            except Exception as e:
                print('error occur')
                print(e)
                new_tab.close()

    def scrapPage(self,
                  city, 
                  province, 
                  page, 
                  pageStart=1, 
                  pageEnd=None, 
                  neighborhoods=None, 
                  csv_file_path='real_estate_data.csv',  
                  TestSingleListing=False, 
                  showLogs=True
                ):
        
        pageNum = pageStart
        if neighborhoods == None:
            neighborhoods = [None]
        for neighborhood in neighborhoods:
            neighborhood = '' if neighborhood is None else neighborhood + '-'
            
            try:
                for pageNum in range(pageStart, pageEnd+1):
                    url = f'https://www.rew.ca/properties/areas/{neighborhood}{city}-{province}/page/{pageNum}'
                    print(f"scraping url: {url}")
                    
                    sleep(1)
                    page.goto(url)

                    listing = page.query_selector_all('.displaypanel')

                    # iterate through listings
                    for i in range(len(listing)):

                        # for testing purposes only, will stop after scraping one listing
                        # if i > 1: return

                        currListing = listing[i]
                        dic_data = self.open_new_tab(page,currListing)

                        # write to given csv
                        write_to_csv(dic_data, column_names, csv_file_path)
                        
                        # print(dic_data)
                        print(f"{i+1}/{len(listing)} Scraped data for address: {dic_data['address']}")

                    # check if next page exist or not
                    # nextPageHtml = page.inner_html('li.paginator-next_page.paginator-control')

                    # if not pageUtils().isNextPageAvailable(nextPageHtml):
                    #     if showLogs: print("next page is not available.")
                    #     break
                    # check if next page exist or not
                    c = page.inner_html('li.paginator-next_page.paginator-control')
                    if not pageUtils().isNextPageAvailable(c): break

                sleep(random.randint(5, 7))

            except Exception as e:
                print(f"page could not be retrieved at url:{url}")
                print(e)
