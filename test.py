print("Hello world")

import requests
response = requests.get('http://api.glassdoor.com/api/api.htm?v=1&format=json&t.p=193675&t.k=dKoyQlorYWm&action=employers&q=software&userip=192.168.43.42&useragent=Chrome/43.0.2357.81', headers={
                               "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36"})
print(response.status_code)

