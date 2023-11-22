from flask import Flask, abort, render_template, request
from vendors.glantix_vendor import Glantix
from vendors.Kenya_computer_vendor import Kenyacomputer

app = Flask(__name__)
app.url_map.strict_slashes = False


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


@app.route('/count/', defaults={'vendor': None})
@app.route('/count/<vendor>')
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
            return str(len({**all_laptops, **all_desktops})), 200
        return 'Seller Not available', 404
    # if nor vendor is specified
    glantix = Glantix()
    all_items_g = glantix.all()

    kenyacomputer = Kenyacomputer()
    all_items_k = kenyacomputer.all()

    return str(len({**all_items_g, **all_items_k}))


@app.route('/laptop/', defaults={'vendor': None})
@app.route('/laptop/<vendor>')
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
    return render_template('display.html', item_dict=all_items, items='Laptop')


@app.route('/desktop/', defaults={'vendor': None})
@app.route('/desktop/<vendor>')
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
    return render_template('display.html', item_dict=all_items, items='Desktop')


@app.route('/all/', defaults={'vendor': None})
@app.route('/all/<vendor>')
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
    return render_template('display.html', item_dict=search_items, items='Laptop and Desktop')



@app.route('/search/', methods=["POST"])
def search():
    '''this is a search function that searches the data by name

    '''
    
    name = request.form.get('searchName').lower()
    glantix = Glantix()
    all_items_g = glantix.all()
    kenyacomputer = Kenyacomputer()
    all_items_k = kenyacomputer.all()

    all_items = {**all_items_g, **all_items_k}


    search_items = {k: v for k, v in all_items.items() if name in k}
    return render_template('display.html', item_dict=search_items, items=name)

@app.route('/compare/<item_1>/<item_2>')
def compare(item_1, item_2):
    glantix = Glantix()
    all_items_g = glantix.all()

    kenyacomputer = Kenyacomputer()
    all_items_k = kenyacomputer.all()
    all_items = {**all_items_g, **all_items_k}
    search_items = {k: v for k, v in all_items.items() if item_1.lower() in k or item_2.lower() in k}
    return render_template('compare.html', item_dict=search_items, item1=item_1, item2=item_2)

@app.route('/')
def home():
    return render_template('base.html')


if __name__ == '__main__':
    app.run(debug=True)
