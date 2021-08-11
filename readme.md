# 此版本已过期, 只作为参考. 请以PDF版本为准.
# api documentation

- ### [authentication](#authentication)
- ### [product](#product)
- ### [container](#container)
- ### [inbound](#inbound)
- ### [order](#order)
- ### [warehouse_list](#warehouse_list)


## authentication
use token authentication: `Authorization: Token {YOUR_API_KEY}`
```
#curl: 
curl -X GET {DOMAIN}/api/inventory/warehouses/ \
    -H "Authorization: Token {YOUR_API_KEY}"

#python3:
headers = {
    'Authorization': 'Token ' + {YOUR_API_KEY}
}
requests.get('{DOMAIN}/api/inventory/warehouses/', headers=headers)
```



## product

- list: get list of products
    - url: /api/inventory/products/
    - method: `GET`
    - params
        - status: `status` of product, e.g. `created`, `approved`
    - sample response:
    HTTP 200 OK
```json
    [{
        "sku": "cus1_test_0001",
        "name": "手机膜 a3390",
        "description": "",
        "dim_length_cm": "14.31",
        "dim_height_cm": "7.09",
        "dim_width_cm": "14.78",
        "weight_kg": "1579.75",
        "status": "approved",
        "created_at": "2021-05-09T17:01:35.663583-07:00",
        "updated_at": "2021-05-26T14:56:52.087130-07:00"
    }]
```
- detail: get details of one product
    - url: /api/inventory/products/{PRODUCT-SKU/ 
    or /api/inventory/products/{PRODUCT-UUID/
    - method: `GET`
    - sample resposne
```json
    {
        "sku": "cus1_test_0005",
        "name": "耳机 a6394",
        "description": "",
        "dim_length_cm": "7.42",
        "dim_height_cm": "5.81",
        "dim_width_cm": "14.19",
        "weight_kg": "1835.16",
        "status": "created",
        "created_at": "2021-05-09T17:01:35.700485-07:00",
        "updated_at": "2021-05-26T15:07:38.294495-07:00"
    }
```

- create: create new product
    - url: /api/inventory/products/
    - method: `POST`
    - data:
        - sku: `Unique slug` stock-keeping unit or product. required.
        - name: `string` product name, chinese ok. required.
        - dim_length_cm: `.2f number` in cm
        - dim_width_cm: `.2f number` in cm 
        - dim_height_cm: `.2f number` in cm
        - width_kg: `.2f number` in kg, required
        - description: `string`, optional
        - dim_unit: `"cm" or "inch"`, required
        - weight_unit: `"kg" or "lb"`, required.
    - samples:
```json
request
    {
        "sku": "cus1_test_0005",
        "name": "耳机 a6394",
        "description": "",
        "dim_length_cm": "7.42",
        "dim_height_cm": "5.81",
        "dim_width_cm": "14.19",
        "weight_kg": "1835.16",
        "dim_unit": "cm",
        "weight_unit": "kg"
    }
```
```json
response HTTP 400
    [
        "Product with SKU cus1_test_0005 exists."
    ]
```
```json
request
    {
        "sku": "cus1_test_0005",
        "name": "耳机 a6394",
        "description": "",
        "dim_length_cm": "7.42",
        "dim_height_cm": "5.81",
        "dim_width_cm": "14.19",
        "weight_kg": "1835.16"
    }
```
```json
response HTTP 400
{
    "dim_unit": [
        "This field is required."
    ],
    "weight_unit": [
        "This field is required."
    ]
}
```
- update: update a product that is not approved or deleted by manager.
    - url: /api/inventory/products/{PRODUCT-UUID}/
    or /api/inventory/products/{PRODUCT-SKU}/
    - method: `PUT`(replace) or `PATCH`(partial update)
    - data: same as date in create. 


## container
- list: list of container
    - url: /api/inventory/containers/
    - method: `GET`
    - params: 
        - status: `created`, `confirmed`, `arrived`, `unloaded`, `returned`
    - sample resposne:
```json
    [
    {
        "warehouse": "rowland2",
        "container_id": "95825496",
        "container_type": "default",
        "priority": "normal",
        "date_eta": null,
        "comment": "",
        "inbounds": [
            {
                "product": "cus1_test_0001",
                "claimed_num_box": 20,
                "claimed_count": 100,
                "comment": "易碎"
            }
        ],
        "status": "created",
        "uuid": "9277e778-083b-4020-9d85-aa8ff00f5564",
        "date_comfirmed_eta": null,
        "date_arrival": null,
        "date_unloading": null,
        "date_return": null
    },
    {
        "warehouse": "rowland2",
        "container_id": "94733495",
        "container_type": "default",
        "priority": "normal",
        "date_eta": null,
        "comment": "",
        "inbounds": [],
        "status": "created",
        "uuid": "6222bbff-d834-45fd-80fe-9282a40a1f79",
        "date_comfirmed_eta": null,
        "date_arrival": null,
        "date_unloading": null,
        "date_return": null
    }]
```
 
- detail: 
    - url /api/inventory/containers/{CONTAINER_ID}/
    - method `GET`
    - sample response:
```json
HTTP 200
    {
        "warehouse": "rowland2",
        "container_id": "80089488",
        "container_type": "default",
        "priority": "normal",
        "date_eta": null,
        "comment": "",
        "inbounds": [],
        "status": "created",
        "uuid": "f7828836-ae41-4bf7-9b5d-e98bad8d881c",
        "date_comfirmed_eta": null,
        "date_arrival": null,
        "date_unloading": null,
        "date_return": null
    }
```
```json
HTTP 404
    {
        "detail": "Not found."
    }
```
- delete: 
    - url /api/inventory/containers/{CONTAINER_UUID}/
    - method: `DELETE`
    - only containers that is 'created' can be deleted.
    - data: no data.

- create: 
    - url /api/inventory/containers/
    - method `POST` 
    - data:
        - warehouse: `name` id of warehosue, required.
        - container_id: `string` container id
        - contaienr_type: `string` container type, omit it or set to "default" if not sure
        - priority: `normal` or `hight`, optional
        - date_eta: Arrival date. `string of data: yyyy-mm-dd` , required.
        - comment: optional
    - samples: 
```json
request
    {
        "warehouse": "rowland2",
        "container_id": "80089488",
        "container_type": "default",
        "priority": "normal",
        "date_eta": "2021-06-01",
        "comment": "this is my comment"
    }
```
```json
response
    {
        "warehouse": "rowland2",
        "container_id": "80089488",
        "container_type": "default",
        "priority": "normal",
        "date_eta": "2021-06-01",
        "comment": "this is my comment",
        "inbounds": [],
        "status": "created",
        "uuid": "f7828836-ae41-4bf7-9b5d-e98bad8d881c",
        "date_comfirmed_eta": null,
        "date_arrival": null,
        "date_unloading": null,
        "date_return": null
    }
```

- update: 
    - url /api/inventory/containers/{CONTAINER_UUID}/
    - method `PUT` / `PATCH`
    - data: same as create
    - samples
```json
request
    {
        "warehouse": "rowland2",
        "container_id": "80089488",
        "container_type": "default",
        "priority": "normal",
        "date_eta": "2021-06-01",
        "comment": "this is my comment"
    }
response
    {
        "warehouse": "rowland2",
        "container_id": "80089488",
        "container_type": "default",
        "priority": "normal",
        "date_eta": "2021-06-01",
        "comment": "this is my comment",
        "inbounds": [],
        "status": "created",
        "uuid": "f7828836-ae41-4bf7-9b5d-e98bad8d881c",
        "date_comfirmed_eta": null,
        "date_arrival": null,
        "date_unloading": null,
        "date_return": null
    }
```




## inbound
inbound api is for customer to add/update/delete an inbound in a container.
- url /api/inventory/inbounds/
- method `POST`
- data:
    - container: container `uuid` e.g. `"9277e778-083b-4020-9d85-aa8ff00f5564"`
    - product: product `sku` e.g. "cus1_test_0001" required.
    - claimed_num_box: `int` how many boxes of current `product` in the `container`. required.
    - count_per_box: `int` how many `products` in a box. required.
    - claimed_total_count: `int` total number of `product` in the `container`. required.
    this value must `count_per_box x claimed_num_box`
    - comment: `string` comment, optional
- return_data: the return data will be the data of the target container.
- delete inbounds: set claimed_total_count, claimed_num_box, count_per_box to 0.
- samples
```json
request
    {
        "container": "9277e778-083b-4020-9d85-aa8ff00f5564",
        "product": "cus1_test_0001",
        "claimed_num_box": 3,
        "count_per_box": 5,
        "claimed_total_count": 100
    }
response
    {
        "count_per_box, claimed_total_count, claimed_num_box are not match"
    }
request
    {
        "container": "9277e778-083b-4020-9d85-aa8ff00f5564",
        "product": "cus1_test_0001",
        "claimed_num_box": 20,
        "count_per_box": 5,
        "claimed_total_count": 100,
        "comment": "易碎"
    }
response
    {
        "warehouse": "rowland2",
        "container_id": "95825496",
        "container_type": "default",
        "priority": "normal",
        "date_eta": null,
        "comment": "",
        "inbounds": [
            {
                "product": "cus1_test_0001",
                "claimed_num_box": 20,
                "claimed_count": 100,
                "comment": "易碎"
            }
        ],
        "status": "created",
        "uuid": "9277e778-083b-4020-9d85-aa8ff00f5564",
        "date_comfirmed_eta": null,
        "date_arrival": null,
        "date_unloading": null,
        "date_return": null
    }
```
    

## order
- list
    - url /api/sales/b2corders/
    - method `GET`
    - params
        - status `created`, `processed`, `confirmed`, `rejected`
- detail
    - url /api/sales/b2corders/{ORDER-UUID}/
    - method `GET`
    - sample response
```json
    {
        "uuid": "233b17e4-ae6a-4b28-8841-55a01008a837",
        "status": "processed",
        "created_at": "2021-05-19T16:55:08.645143-07:00",
        "product": "5d39deea-432b-4f60-99f2-636d2e12cfa8",
        "order_date": null,
        "qty": 5,
        "order_num": "da197fb1-30de-4e1d-8bd1-a803c38163f6",
        "warehouse": "ee527b2a-d5cf-480f-aaa8-e59f9bdee950",
        "recipient_addr": {
            "name": "default name",
            "email": "",
            "phone": "not provided",
            "company": "",
            "street1": "stree address",
            "street2": "",
            "country": "US",
            "state": "CA",
            "city": "los an",
            "zip_code": "48673"
        },
        "warehosue": "rowland2",
        "itemstr": "手机壳 sk7171x5",
        "shipment": {
            "tracking_number": "82531069261",
            "courier": "ups"
        }
    }
```
- create
    - url /api/sales/b2corders/
    - method `POST`
    - data
        - product: product `SKU`, required
        - qty: `int` quantity of product, required
        - order_num: the order number in your system, required.
        - warehouse: warehouse name, required.
        - recipient_addr: the recipient address
            - name `required`
            - email `optional`
            - phone `optional`
            - company `optional`
            - street1 `required`
            - street2 `optional`
            - country `required`
            - state `required`
            - city `required`
            - zip_code `required`
        - other data are readonly or infomation.
    - samples
```json
request
    {
        "product": "cus1_test_0004",
        "order_date": "2021-05-10",
        "qty": 1,
        "order_num": "29d67323-0501-46ff-9c38-ee1baeae206b",
        "warehouse": "queen1",
        "recipient_addr": {
            "name": "default name",
            "email": "",
            "phone": "not provided",
            "company": "",
            "street1": "stree address",
            "street2": "",
            "country": "US",
            "state": "CA",
            "city": "los an",
            "zip_code": "48673"
        }
    }
response
    {
        "uuid": "bf3b2058-030b-4c48-82e2-57f6dcab3ce8",
        "status": "created",
        "created_at": "2021-05-26T17:45:18.346961-07:00",
        "product": "cus1_test_0004",
        "order_date": "2021-05-10",
        "qty": 1,
        "order_num": "29d67323-0501-46ff-9c38-ee1baeae206b",
        "warehouse": "queen1",
        "recipient_addr": {
            "name": "default name",
            "email": "",
            "phone": "not provided",
            "company": "",
            "street1": "stree address",
            "street2": "",
            "country": "US",
            "state": "CA",
            "city": "los an",
            "zip_code": "48673"
        },
        "itemstr": "手机壳 uu3523x1",
        "shipment": null
    }
```

- update
    - url /api/sales/b2corders/{ORDER-UUID}/
    - method `POST`
    - data: same as data to create.

## warehouse_list
Show list of your available warehouses. Warehouses' names are unique.
- list: `GET` /api/inventory/warehouses/
```json
[
    {
        "name": "rowland2",
        "address": "uPO0fC, HVE4, CA UObPj"
    },
    {
        "name": "Denver1",
        "address": "OzTDZu, OKBt, CA OVovX"
    },
    {
        "name": "queen1",
        "address": "ZrtZJK, p5DW, CA b9iZy"
    }
]
```