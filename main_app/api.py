import requests

'''
A separate script to test the API. Just incase tools like Postman fails !
From the root directory, just run: python3 main_app/api.py


READ THE DOCUMENTATION FIRST!


'''

# GET method - 'test/ endpoint'

url = 'http://127.0.0.1:8000/test/'
headers = {'Authorization': 'Token <TOKEN-HERE>'}

r = requests.get(url, headers=headers)
print(r.status_code)
print(r.reason)
print(r.content)



# POST method - 'register/ endpoint'
# You get auth-token in login, not here

url = 'http://127.0.0.1:8000/register/'
headers = {'Authorization': 'Token <TOKEN-HERE>'}

data = {
    'email': 'email1@gmail.com, email2@gmail.com, email3@gmail.com', 
    'username': 'username-here',
    'password': 'password-here',
}

r = requests.post(url, data=data, headers=headers)
print(r.status_code)
print(r.reason)
print(r.content)


# POST method - 'login/ endpoint'
# You get the auth-token after successful login

url = 'http://127.0.0.1:8000/login/'
headers = {'Authorization': 'Token <TOKEN-HERE>'}

data = {

    'username': 'username-here',
    'password': 'password-here',
}

r = requests.post(url, data=data, headers=headers)
print(r.status_code)
print(r.reason)
print(r.content)




# POST method - 'send multiple emails endpoint'

url = 'http://127.0.0.1:8000/'
headers = {'Authorization': 'Token <TOKEN-HERE>'}

data = {
    'email-receiver': 'email1@gmail.com, email2@gmail.com, email3@gmail.com',
    'email-subject': 'Sent from API',
    'email-body': 'Hello UdictiMailer',
}

r = requests.post(url, data=data, headers=headers)
print(r.status_code)
print(r.reason)
print(r.content)
