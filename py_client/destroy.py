import requests
product_id = input("what is the product id you want to use ?")
try:
    product_id = int(product_id)
except:
    print(f'the {product_id} is not valid')

if product_id:

    endpoints = f"http://127.0.0.1:8000/api/products/{product_id}/destroy/"
    get_response = requests.delete(endpoints)
    print(get_response.status_code, get_response.status_code == 204)