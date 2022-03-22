import requests

endpoints = "http://127.0.0.1:8000/api/products/all"

get_response = requests.get(endpoints)

print(get_response.json())