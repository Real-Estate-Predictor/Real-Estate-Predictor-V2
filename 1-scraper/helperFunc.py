from xmlrpc.client import Boolean
from bs4 import BeautifulSoup
from collections import OrderedDict
import json
import csv

class Utils:
    def write_to_csv(self, data: dict):

        li = []
        for (k,v) in data.items():
            li.append(v)

        with open('house_data.csv', mode='a',newline='') as data_file:
            data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            data_writer.writerow(li)



    def get_info(self, source_code: str) -> dict:
        # returns a dictionary then writes

        print("get_info() called")

        # turn the source code into a bfs object
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
                key = section.find_all('div')[0].text.strip('\n')
                val = section.find_all('div')[1].text.strip('\n')
                data_dic[key] = val

        if 'List Price' in data_dic:
            del data_dic['List Price']

        # self.write_to_csv(data_dic)

        return data_dic

    def isNextPageAvailable(self, source_code: str) -> Boolean:
        soup = BeautifulSoup(source_code, 'html.parser')
        if soup.find('a') == None:
            return False
        return True