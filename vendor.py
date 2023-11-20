#!usr/bin/python3
''' this module define two vendors and the methods to get the
items they sell (the laptop and the desktop'''

from bs4 import BeautifulSoup


class Vendor():
    ''' this is the base model for all vendors'''
    _laptops = {}
    _desktops = {}

    def item(self, item, name=None):
        ''' this returns all laptops or the desktop for the Glantix vendor
            
            Parameter:
            item (str) : Type of items to load. Can be 'laptop' or 'desktop'.
            name (str, optional) : this is a name of a laptop  to be searched
            Return a dictionary with the name of the item as the key
        '''

        if name is None:         
            self.load_items(item)
            return self._laptops if item == 'laptop' else self. _desktops
        
        if name:
            self.load_items(item)
            new_items = self._laptops if item == 'laptop' else self. _desktops

            return {k: v for k, v in new_items.items() if name.lower() in k}

    def all(self):
        ''' return all item of this vendor both laptops and dektops'''
        all_laptops = self.item('laptop')
        all_desktops = self.item('desktop')
        return {**all_desktops, **all_laptops}
