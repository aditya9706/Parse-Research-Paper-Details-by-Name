from ph2 import ParseHub
import requests
import json

params = {
  "api_key": "t-N_kGgKXHF4",
}

r = requests.post("https://www.parsehub.com/api/v2/runs/txTSnQe1YU9Z/cancel",data = params)
print(r.text)