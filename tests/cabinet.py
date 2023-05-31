import requests


r = requests.get("http://127.0.0.1:8000/requests", params={"limit": 1})

print(r.json())