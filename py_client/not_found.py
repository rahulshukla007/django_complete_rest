import requests

endpoints = "http://127.0.0.1:8000/api/products/alt/1656977"

get_response = requests.get(endpoints)

print(get_response.json())