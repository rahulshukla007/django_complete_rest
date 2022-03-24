#it will handle both get & post requests
import requests
from getpass import getpass

auth_endpoints = "http://127.0.0.1:8000/api/auth/"
username = input("please ennter a username: ")
password = getpass("please enter the password: ")

auth_response = requests.post(auth_endpoints, json={"username":username, 'password':password})

print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization":f"Bearer {token}"
    }
    endpoints = "http://127.0.0.1:8000/api/products/li"

    get_response = requests.get(endpoints, headers=headers)

    print(get_response.json())