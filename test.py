print("Hello world")

from pip.vendor import requests
response = requests.get('http://api.glassdoor.com/api/api.htm?v=1.1&format=json&t.p=193675&t.k=dKoyQlorYWm&action=employers&q=software&userip=192.168.43.42&useragent=Chrome/%2F4.0')
print(response.status_code)
