import uuid
from auth import config

from products import get_product_list


def create_fba_order():
    # get a product sku for testing
    sku = get_product_list()[0]['sku']
    # get a warehouse name for testing
    warehouse_name = config.get_warehouses()[0]['name']
    url = '/api/sales/fbaorders/'
    data = {
        'product': str(sku),
        # total number of product
        'count': 10,
        'qty_per_box': 2,
        'qty_box': 5,
        'order_num': str(uuid.uuid4()),
        'warehouse_code': 'abcd',
        'warehouse': warehouse_name,
        # BoxLabel, Box+ProductLabel or none
        'operation_warehouse': 'BoxLabel', 
        # AmazonUPS, AmazonPickup, AmazonLTL
        'order_type': 'AmazonLTL',
        'recipient_address': {
            'name': 'recipient name',
            'email': 'email@email.com',
            'phone': '1234567890', 
            'street1': '1234 street',
            'city': 'City Name', 
            # state code
            'state': 'CA', 
            'zip_code': '12345', 
            'country': 'US', 
        }
    }
    res = config.post(url, data)
    print(res.json())


def get_fbaorder_list():
    """ get FBA order list"""
    res = config.get('/api/sales/fbaorders/')
    print('Total number of FBA orders: ', len(res.json()))


def run():
    create_fba_order()
    get_fbaorder_list()


if __name__ == '__main__': run()
