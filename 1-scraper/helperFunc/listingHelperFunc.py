from xmlrpc.client import Boolean
from bs4 import BeautifulSoup
from collections import OrderedDict
from Logger import Logger
import json
import csv
from helperFunc.columnNames import column_names

class listingUtils:
    def write_to_csv(self, data: dict):
        with open('house_data.csv', mode='a',newline='') as data_file:
            data_writer = csv.DictWriter(data_file, fieldnames=column_names)

            # uncomment line below to print the column_names
            # data_writer.writeheader()
            data_writer.writerow(data)

    # returns a dictionary then writes
    # turn the source code into a bfs object
    def get_info(self, source_code: str) -> dict:
        soup = BeautifulSoup(source_code, 'html.parser')

        table_data = []

        data_dic = {}

        # get address
        address = soup.findAll("div", {"class": "listingheader-address"})
        print(address)
        # save address to list
        address_text = address[0].text
        table_data.append(['address',address_text])

        # save address to dictionary 
        # print('ADDRESS:',address_text, type(address_text))
        data_dic['address'] = address_text

        # get price
        price = soup.findAll("div", {"class": "listingheader-price"})

        # save price to list
        price_text = price[0].text
        table_data.append(['price',price_text])
        # save price to dictionary
        data_dic['price'] = price_text

        all_lineddisplay = soup.find_all("div", {"class": "lineddisplay"})
        
        for lineddisplay in all_lineddisplay:
            for section in lineddisplay.find_all('section'):
                key = section.find_all('div')[0].text.strip('\n').lower()
                val = section.find_all('div')[1].text.strip('\n').lower()
                
                data_dic[self.formattingKey(key)] = val

        self.removeUselessColumn(data_dic)
        
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