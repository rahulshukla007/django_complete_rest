import requests

endpoints = "http://127.0.0.1:8000/api/"

get_response = requests.post(endpoints, json={'content':'this is ok'})

# print(get_response.text)
# print(get_response.status_code)
print(get_response.json())