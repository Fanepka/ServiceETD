import json
import requests


data = {
    "email": "play.fanner@gmail.com",
    "password": "123456"
}

r = requests.get("http://127.0.0.1:8000/api/addresses", headers={"token": "12345"})

print(r.status_code)

