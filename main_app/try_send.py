import requests

url = 'http://udictimailer.herokuapp.com/send/'
headers = {'Authorization': 'Token 0d328fbb8812b3552e8053109d0adcd26c1cd55b'}

data = {
    'email-receiver': '2001stany@gmail.com',
    'email-subject': 'Sent from API',
    'email-body': 'Hello UdictiMailer hhhhhhhhhhhhhhhhhhhhhhhhkdddddddddddddddddfffffffffkdfdkfdkhfkd',
}

r = requests.post(url, data=data, headers=headers)
print(r.status_code)
print(r.reason)
print(r.content)