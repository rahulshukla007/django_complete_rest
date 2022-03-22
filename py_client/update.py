import requests

endpoints = "http://127.0.0.1:8000/api/products/1/update/"
data = {"title":"solar panel", "price":35}
get_response = requests.put(endpoints, json=data)
print(get_response.json())