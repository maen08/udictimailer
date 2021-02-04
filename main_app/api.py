import requests

url = 'http://127.0.0.1:8000/test/'
headers = {'Authorization': 'Token 4197e04e373405ba172419afe7f0a5c1578d0739'}
r = requests.get(url, headers=headers)
print(r.status_code)
print(r.content)