import requests

url = 'http://127.0.0.1:8000/test/'
headers = {'Authorization': 'Token faa0f3cead3f8e2e6dcd9e5511f7034297c30632'}
r = requests.get(url, headers=headers)
print(r.status_code)
print(r.content)