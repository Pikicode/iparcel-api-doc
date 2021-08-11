import uuid

from auth import config

url = '/api/inventory/products/'
random_sku = str(uuid.uuid4())

def create_product(sku=None):
    """create a product"""
    data = {
        'sku': sku or random_sku, # unique sku.
        'name': 'TEST PRODUCT', #
        'description': '',
        "dim_length_cm": 5,
        "dim_height_cm": 6,
        "dim_width_cm": 7,
        "weight_kg": 1.5,
        "dim_unit": 'cm',
        "weight_unit": 'kg',
    }
    res = config.post(url, data)
    print(res.json())


def get_single_product(sku):
    """get data of single product."""
    res = config.get(url + sku + '/')
    print(res.json())
    return res.json()


def get_product_list():
    res = config.get(url)
    print(len(res.json()))
    return res.json()


def run():
    create_product()
    get_single_product(random_sku)
    get_product_list()


if __name__ == '__main__': run()