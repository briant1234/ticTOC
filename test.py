print("Hello world")
import json
import requests
response = requests.get('http://api.glassdoor.com/api/api.htm?v=1&format=json&t.p=193675&t.k=dKoyQlorYWm&action=employers&q=software&userip=192.168.43.42&useragent=Chrome/43.0.2357.81', headers={
                               "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36"})
login = requests.get("https://app.joinhandshake.com/auth?auth=84")
eventresponse = requests.get("https://app.joinhandshake.com/api/v1/events", headers = {"Authentication"})
self.changes = {}
if eventresponse.status_code == 401:    
    eventresponse = requests.get("https://app.joinhandshake.com/api/v1/events", auth=HTTPBasicAuth('user', 'pass'))

print(response.status_code)
print(login.status_code)
print(eventresponse.status_code)
data = response.json()
f=open('response.json','w')
print(data)
formatted=str(json.dumps(data,sort_keys=False,indent=4, separators=(',', ': ')))
f.write(formatted)