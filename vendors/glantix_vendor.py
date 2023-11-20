#!/usr/bin/python3
'''this module define a vendor call Glantix'''
from vendor import Vendor
from bs4 import BeautifulSoup


class Glantix(Vendor):
    ''' this class defines a vendor called kilimall'''

    def load_items(self, item):
        '''it loads all the item of the vendor from the
        file and stores in memory

        Parameter
        - item (str, optional): Type of items to load.
        Can be 'laptop' or 'desktop'.
        '''
        item_file = '../static_data/glantix_laptop' if item == 'laptop' \
                    else '../static_data/glantix_desktop'

        with open(item_file, 'r') as f:
            soup = BeautifulSoup(f, 'html.parser')
            all_div = soup.find_all('div', {'class': 'product-card'})
            for laptop in all_div:
                new = {}
                name = laptop.a.get('title')
                new['name'] = name
                new['link'] = laptop.a.get('href')
                new['img_link'] = laptop.img.get('src')
                new['price'] = laptop.find('span', {'special-price'}).text.strip('\n KSH\xa0')
                new['Vendor'] = self.__class__.__name__

                key = '{}.{}'.format(name, self.__class__.__name__)
                if item == 'laptop':
                    self._laptops[key.lower()] = new
                else:
                    self._desktops[key.lower()] = new
