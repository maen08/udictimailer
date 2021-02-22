import requests

url = 'http://127.0.0.1:8000/test/'
headers = {'Authorization': 'Token f31ad0ec5a17baa1c419d5ab8d424e5b3a408087'}
r = requests.get(url, headers=headers)
print(r.status_code)
print(r.content)
