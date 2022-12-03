import requests

endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anythingqsd"
endpoint = "http://127.0.0.1:8000/api/"

# get_response = requests.get(endpoint, params={"abc":123}, json={"product_id": 123 })  # HTTP request
get_response = requests.get(endpoint, json={"product_id": 123})

# print(get_response.headers)
# print(get_response.text) # Print contain of endpoint

print(get_response.json()) # Print contain of endpoint
print(get_response.status_code) # Print contain of endpoint
