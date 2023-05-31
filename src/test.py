import requests
import json


data = {
    "name": "plywood",
    "age": 18
}

r = requests.post("http://127.0.0.1:8000/requests", data=json.dumps(data))

print(r)