import requests
import json

url = "http://127.0.0.1:8000/api/api/"

response = requests.get(url)

data = json.loads(response.text)

print(data)
