import requests

url = 'http://127.0.0.1:8000/send/'
headers = {'Authorization': 'Token 51dbcaf6ee8afcb191dcf853a3a3c638fedb0edf'}

data = {
    'email-receiver': 'jackkweyunga@gmail.com',
    'email-subject': 'Sent from API',
    'email-body': 'Hello UdictiMailer hhhhhhhhhhhhhhhhhhhhhhhhkdddddddddddddddddfffffffffkdfdkfdkhfkd',
}

r = requests.post(url, data=data, headers=headers)
print(r.status_code)
print(r.reason)
# print(r.content)