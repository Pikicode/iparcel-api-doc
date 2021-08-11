import uuid, random


from auth import config

url = '/api/inventory/containers/'

random_container_id = str(uuid.uuid4())


def get_warehouses():
    """get available warehouses"""
    res = config.get('/api/inventory/warehouses/')
    print('Warehouse List: ', res.json())
    return res.json()


def create_container(warehouse_name):
    data = {
        # name from get_warehouses, required.
        'warehouse': warehouse_name, 
        # unique contaienr id(slug), required.
        'container_id': random_container_id,
        # container_type: 45HQ, 40HQ, or 'default', required.
        'container_type': 'default',
        # priority: string normal/high, optional
        # date_eta: string(yyyy-mm-dd), optional 
        # comment: string, optinal
    }
    res = config.post(url, data)
    print("created container info: ", res.json())


def get_container_list():
    res = config.get(url)
    print('Total number of containers: ', len(res.json()))


def get_container(container_id):
    """retrieve single contaienr."""
    res = config.get(url + container_id + '/')
    print('Container info: ')
    try: print(res.json())
    except: print('failed to get container with id: ', container_id)


def edit_container(container_id):
    data = {
        'comment': 'new comment.'
    }
    res = config.path(url + container_id + '/', data)
    print('Container info after change.')
    print(res.json())


def run():
    warehouses = get_warehouses()
    if len(warehouses) == 0:
        print('no available warehouse.')
        return 1
    warehouse_name = warehouses[0]['name']
    print('Use warehouse: ', warehouse_name)
    create_container(warehouse_name)
    get_container_list()
    get_container(random_container_id)
    edit_container(random_container_id)

if __name__ == '__main__': run()

