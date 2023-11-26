from flask import Flask, abort, jsonify, request
from vendors.glantix_vendor import Glantix
from vendors.Kenya_computer_vendor import Kenyacomputer
from api.v1.views import app_views


def seller_class(vendor):
    '''perform common logic to all view function
    and return a class that matches the vendor
    '''
    vendor_class = {'glantix': Glantix, 'kenyacomputer': Kenyacomputer}
    vendor_lower = vendor.lower()
    v_class = vendor_class.get(vendor_lower, None)
    if v_class:
        vend = v_class()
        return vend
    return None


@app_views.route('/count/', defaults={'vendor': None})
@app_views.route('/count/<vendor>')
def count(vendor):
    ''' counts the number of items that a vendor has
    - parameter:
    vendor:(string) this the name of the vendor it can eiter be
                    Glantix or Kenyacomputer

    if vendor is none it will return the total items of all vendors
    '''
    if vendor:
        vend = seller_class(vendor)
        if vend:
            all_laptops = vend.item('laptop', vendor)
            all_desktops = vend.item('desktop', vendor)
            return ({vendor: str(len({**all_laptops, **all_desktops}))}), 200
        abort (404,'Seller Not available')
    # if nor vendor is specified
    glantix = Glantix()
    all_items_g = glantix.all()

    kenyacomputer = Kenyacomputer()
    all_items_k = kenyacomputer.all()
    
    count = {}
    all_items = {**all_items_g, **all_items_k}

    for k, v in all_items.items():
        if 'glantix' in k:
            count['Glantix'] = count.get('Glantix', 0) + 1
        if 'kenyacomputer' in k:
            count['KenyaComputer'] = count.get('KenyaComputer', 0) + 1

    return jsonify(count)


@app_views.route('/laptop/', defaults={'vendor': None})
@app_views.route('/laptop/<vendor>')
def laptop(vendor):
    '''return the laptops owned by specific vendor

    -parameter
    vendor:(string) this the name of the vendor it can eiter be
                        Glantix or Kenyacomputer

    if vendor is none it will return the total items of all vendors
    '''
    if vendor:
        vend = seller_class(vendor)
        if vend:
            all_laptops = vend.item('laptop', vendor)
            return all_laptops
        return 'Seller Not available', 404

    # if no vendor is specified
    glantix = Glantix()
    all_items_g = glantix.item('laptop', 'glantix')
    kenyacomputer = Kenyacomputer()
    all_items_k = kenyacomputer.item('laptop', 'kenyacomputer')

    all_items = {**all_items_g, **all_items_k}
    return jsonify(all_items)


@app_views.route('/desktop/', defaults={'vendor': None})
@app_views.route('/desktop/<vendor>')
def desktop(vendor):
    '''return the desktops owned by specific vendor

    -parameter
    vendor:(string) this the name of the vendor it can eiter be
    Glantix or Kenyacomputer

    if vendor is none it will return the total items of all vendors
    '''
    if vendor:
        vend = seller_class(vendor)
        if vend:
            all_desktops = vend.item('desktop', vendor)
            return all_desktops
        abort(404, 'Seller Not available')
    # if no vendor is specified
    glantix = Glantix()
    all_items_g = glantix.item('desktop', 'glantix')
    kenyacomputer = Kenyacomputer()
    all_items_k = kenyacomputer.item('desktop', 'kenyacomputer')
    all_items = {**all_items_g, **all_items_k}
    return jsonify(all_items)


@app_views.route('/all/', defaults={'vendor': None})
@app_views.route('/all/<vendor>')
def all_items(vendor):
    '''return all items owned by the vendor

        -parameter
     vendor:(string) this the name of the vendor it can eiter be
     Glantix or Kenyacomputer
     if vendor is none it will return the total items of all vendors
     '''
    if vendor:
        vend = seller_class(vendor)
        if vend:
            all_desktops = vend.item('desktop', vendor)
            all_laptops = vend.item('laptop', vendor)
            return {**all_laptops, **all_desktops}
        abort(404, 'Seller Not available')

    # if nor vendor is specified
    glantix = Glantix()
    all_items_g = glantix.all()

    kenyacomputer = Kenyacomputer()
    all_items_k = kenyacomputer.all()

    search_items = {**all_items_g, **all_items_k}
    return jsonify(search_items)



@app_views.route('/search/', methods=["GET"])
@app_views.route('/search/<name>', methods=["GET"])
def search(name=""):
    '''this is a search function that searches the data by name

    '''
    
    glantix = Glantix()
    all_items_g = glantix.all()
    kenyacomputer = Kenyacomputer()
    all_items_k = kenyacomputer.all()

    all_items = {**all_items_g, **all_items_k}
    

    search_items = all_items
    return jsonify(search_items)

@app_views.route('/compare/<item_1>/<item_2>')
def compare(item_1, item_2):
    glantix = Glantix()
    all_items_g = glantix.all()

    kenyacomputer = Kenyacomputer()
    all_items_k = kenyacomputer.all()
    all_items = {**all_items_g, **all_items_k}
    search_items = {k: v for k, v in all_items.items() if item_1.lower() in k or item_2.lower() in k}
    return jsonify(search_items)

