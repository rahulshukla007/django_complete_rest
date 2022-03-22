import requests

endpoints = "http://127.0.0.1:8000/api/products/"

data = {"title":"bulb"}
get_response = requests.post(endpoints, json= data)

# print(get_response.text)
# print(get_response.status_code)
print(get_response.json())