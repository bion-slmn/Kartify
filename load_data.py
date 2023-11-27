#!/usr/bin/python3
from vendors.phonex_vendor import Phonex
from vendors.smartbuy_vendor import Smartbuy


from vendors import storage
#storage.drop()

# loading items into memory
Smartbuy.load_items('desktop')
Phonex.load_items('desktop')
Smartbuy.load_items('laptop')
Phonex.load_items('laptop')
