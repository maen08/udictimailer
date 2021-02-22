import requests

'''
A separate script to test the API. Just incase tools like Postman fails !

'''

# GET method - 'test/ endpoint'

url = 'http://127.0.0.1:8000/test/'
headers = {'Authorization': 'Token <TOKEN-HERE>'}

r = requests.get(url, headers=headers)
print(r.status_code)
print(r.content)



# POST method - 'register/ endpoint'

url = 'http://127.0.0.1:8000/register/'
headers = {'Authorization': 'Token <TOKEN-HERE>'}

data = {
    'email': '2001stany@gmail.com, doccasheby@gmail.com',
    'username': 'send from api',
    'password': 'hello'
}

r = requests.post(url, data=data, headers=headers)
print(r.status_code)
print(r.reason)


# POST method - 'login/ endpoint'

url = 'http://127.0.0.1:8000/login/'
headers = {'Authorization': 'Token <TOKEN-HERE>'}

data = {

    'username': 'send from api',
    'password': 'hello'
}

r = requests.post(url, data=data, headers=headers)
print(r.status_code)
print(r.reason)




# POST method - 'send multiple emails endpoint'

url = 'http://127.0.0.1:8000/'
headers = {'Authorization': 'Token <TOKEN-HERE>'}

data = {
    'email-receiver': '2001stany@gmail.com, doccasheby@gmail.com',
    'email-subject': 'send from api',
    'email-body': 'hello'
}

r = requests.post(url, data=data, headers=headers)
print(r.status_code)
print(r.reason)
