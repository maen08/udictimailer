import requests

'''
A separate script to test the API. Just incase tools like Postman fails !


'''

# GET method - 'test/ endpoint'

# url = 'http://127.0.0.1:8000/test/'
# headers = {'Authorization': 'Token f31ad0ec5a17baa1c419d5ab8d424e5b3a408087'}
# r = requests.get(url, headers=headers)
# print(r.status_code)
# print(r.content)



# post method

url = 'http://127.0.0.1:8000/'

data = {
    'email-receiver': '2001stany@gmail.com, doccasheby@gmail.com',
    'email-subject': 'send from api',
    'email-body': 'hello'
}

r = requests.post(url, data=data)
print(r.status_code)
print(r.reason)