import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json={"title": "Hello World","content": "Django POST request", "price": 100})
# print(get_response.text)

#HTTP Response
print(get_response.json())
# print(get_response.status_code)