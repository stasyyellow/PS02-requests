import requests
import pprint

params = {
    'userId' : '1'
}

response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)

print("Cтатус код:", response.status_code)

response_json = response.json()
pprint.pprint(response_json)
