from bs4 import BeautifulSoup

from data_scraping.helperFunc.utils import exception_handler


class ListingUtils:


    # returns a dictionary then writes
    # turn the source code into a bfs object
    @exception_handler
    def get_info(self, source_code: str) -> dict:
        soup = BeautifulSoup(source_code, 'html.parser')

        data_dic = {}

        # get address
        address_text = soup.find('h1', class_='listingheader-address').text.strip()
        data_dic['address'] = address_text

        # get price
        price_text = soup.find('div', class_='listingheader-price').text.strip()
        data_dic['price'] = price_text

        all_lineddisplay = soup.find_all("div", {"class": "lineddisplay"})
        
        for lineddisplay in all_lineddisplay:
            for section in lineddisplay.find_all('section'):
                key = section.find_all('div')[0].text.strip('\n').lower()
                val = section.find_all('div')[1].text.strip('\n').lower()
                
                data_dic[self.formattingKey(key)] = val
                # print(data_dic[self.formattingKey(key)])
        
        return data_dic

    # format key, replace whitespace with underscore
    def formattingKey(self, key) -> str:
            key = key.replace(" ", "_")

            if 'gross_taxes' in key: key = 'gross_tax'
            elif 'feature' in key: key = 'feature'
            
            return key
    
    # remove useless field
    def removeUselessColumn(self, data_dic):
        data_dic.pop('list_price', None)
        data_dic.pop('secondary_broker', None)
        data_dic.pop('secondary_agent', None)
        data_dic.pop('primary_agent', None)
        data_dic.pop('primary_broker', None)