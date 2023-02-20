from xmlrpc.client import Boolean
from bs4 import BeautifulSoup
from helperFunc.listingHelperFunc import listingUtils 
from collections import OrderedDict
from locationName.vancouver.vancouverWest import vancouver_west_neighbourhoods
from time import sleep
import random
import json
import csv

class pageUtils:
    def isNextPageAvailable(self, source_code: str) -> Boolean:
        soup = BeautifulSoup(source_code, 'html.parser')
        return False if soup.find('a') == None else True
    
    def scrapPage(self,  city, province, page, pageStart=1, pageEnd=None, neighborhood=None):
        for neighborhood in vancouver_west_neighbourhoods:
            pageNum = pageStart
            neighborhood = '' if neighborhood is None else neighborhood + '-'
            while True:
                url = f'https://www.rew.ca/properties/areas/{neighborhood}{city}-{province}/page/{pageNum}'
                page.goto(url)      
                listing = page.query_selector_all('.displaypanel')

                for i in range(len(listing)):
                # for dev
                    #if i == 1: break
                    currListing = listing[i]
                    # open listing in new tab
                    with page.context.expect_page() as tab:
                        try: 
                            currListing.click(modifiers=['Meta'])
                            new_tab = tab.value
                            new_tab.wait_for_load_state("networkidle") 
                            new_tab.wait_for_load_state("domcontentloaded")

                            html1 = new_tab.inner_html('div.col-xs-12.col-md-8')
                            dic_data = listingUtils().get_info(html1)
                            sleep(random.randint(2, 5))
                            listingUtils().write_to_csv(dic_data)
                            # print(dic_data.keys())
                            new_tab.close()
                        except:
                            print('error occur')
                            new_tab.close()
                # check if next page exist or not
                c = page.inner_html('li.paginator-next_page.paginator-control')

                if pageEnd is not None and pageEnd == pageNum: break
                if not pageUtils().isNextPageAvailable(c): break
                
                pageNum+=1
                sleep(random.randint(5, 7))
