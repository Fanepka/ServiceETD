import requests
import json


r = requests.post("http://127.0.0.1/ticket", data=json.dumps({"id": 1, "name": "Test"}))

print(r.content)