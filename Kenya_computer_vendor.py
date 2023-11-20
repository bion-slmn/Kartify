#!/usr/bin/python3
''' this defines a class KenyaComputer'''
from vendor import Vendor
from bs4 import BeautifulSoup


class Kenyacomputer(Vendor):
    ''' this class defines acomputer sold at Kenya computer'''

    def load_items(self, item):
        '''it loads all the item of the vendor from the file
        and stores in memory

        Parameter
        - item (str, optional): Type of items to load.
        Can be 'laptop' or 'desktop'
        '''
        item_file = 'static_data/Kenya_computers_laptop' if item == 'laptop' \
                    else 'static_data/Kenya_computers_desktop'

        with open(item_file, 'r') as f:
            soup = BeautifulSoup(f, 'html.parser')
            all_div = soup.find_all('div', {'class': 'col-inner'})
            for laptop in all_div:
                new = {}
                name = laptop.img.get('alt')
                new['name'] = name
                new['link'] = laptop.a.get('href')
                new['img_link'] = laptop.img.get('src')
                new['price'] = laptop.find('bdi').text.strip('KSHh\n     ')

                key = '{}.{}'.format(name, self.__class__.__name__)
                if item == 'laptop':
                    self._laptops[key.lower()] = new
                else:
                    self._desktops[key.lower()] = new
