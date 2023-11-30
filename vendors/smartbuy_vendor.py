#!/usr/bin/python3
''' this defines a class Smartbuy'''
from vendors.vendor import Vendor, Base
from bs4 import BeautifulSoup
import requests


class Smartbuy(Vendor, Base):
    ''' this class defines acomputer sold at Kenya computer'''

    __tablename__ = 'smartbuy'

    @classmethod
    def load_items(cls, item):
        '''it loads all the item of the vendor from the file
        and stores in memory

        Parameter
        - item (str, optional): Type of items to load.
        Can be 'laptop' or 'desktop'
        '''
        from vendors import storage
        url_laptop = 'https://smartbuy.co.ke/product-category/laptops/'
        url_desktop = 'https://smartbuy.co.ke/product-category/desktops/'
        url = url_laptop if item == 'laptop' else url_desktop

        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            all_div = soup.find_all('div',
                                    class_='product-outer product-item__outer')
            for laptop in all_div:
                new = {}
                name = laptop.h2.text
                new['name'] = name
                new['img_link'] = laptop.img.get('src')
                link = laptop.find(
                        'a',
                        class_='woocommerce-LoopProduct-link woocommerce-loop-product__link')
                new['link'] = link.get('href')
                new['price'] = laptop.find('bdi').get_text().strip('KSHh')
                new['vendor'] = cls.__name__
                new['catergory'] = 'laptop' if item == 'laptop' else 'desktop'

                obj = cls(**new)
                storage.new(obj)
                storage.save()

        except Exception as e:
            raise Exception(e)
