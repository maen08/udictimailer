# UdictiMailer API


[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/maen08)

API that helps to send the multiple emails (currently, used only for UDICTI official projects). Easy to integrate in your project !



### INTRODUCTION
---
- #### Allowed HTTP requests:

  - GET - Get the list of resource
  - POST - Update the resource


- #### Description of some HTTP responses:

  - `200 OK `- the request was successful 
  - `201 Created `- the request was successful and a resource was created.
  - `400 Bad Request` - the request could not be understood or was missing required parameters.
  - `401 Unauthorized` - authentication failed or user doesn't have permissions for requested operation.
  - `403 Forbidden` - access denied.
  - `404 Not Found` - resource was not found.

##
##

### ENDPOINTS

Endpoint | HTTP Method | Parameter | Description
| ------ | ------ | ------ | ------ |
| register/ | POST | `email`, `username`, `password` | Endpoint to register user. All parameters are required. Make sure you are using the same names even if in DOM (HTML elements eg. name="email")
| login/ | POST | `username`, `password` | Pass the same username and password which used to register a particular user. Any other different parameter will result an error. Successful logged in user will obtain `token`
| test/ |GET | NULL | This is the endpoint just to test your `token` and all setup if everything works fine. You must get `200 OK` response
| / | GET | `email-subject`, `email-body`, `email-receiver` | The endpoint that sends email. Pass the parameters required and the `token` to send emails.

##
##

### DATA TYPES OF PARAMETERS
---
- email `(String)` : Unique email per user
-  username `(String)` : Unique username per user
-   password `(String)` : Adviced to be strong password
-   email-subject `(String)`: The subject of email
-   email-body `(String)`: The body itself
-   email-receiver `(String)`: Receiver's emails. May be multiple emails separated by a comma (,)

##
##

### ENDPOINT TESTS
---
You can test the endpoints and HTTP requests using any tool (Postman, being so common) that you're comfortable with. This documentation uses `requests` (a Python package) to perform some of the methods, just to give an example.

Feel free to use any language with any technology during testing.

##### Registration endpoint (register/)

```sh
import requests

url = 'http://127.0.0.1:8000/register/'

data = {
    'email': 'email@gmail.com', 
    'username': 'username-here',
    'password': 'password-here',
}

r = requests.post(url, data=data)
print(r.status_code)
print(r.reason)
print(r.content)
```


##### Login endpoint (login/)

```sh
import requests

url = 'http://127.0.0.1:8000/login/'

data = {

    'username': 'username-here',
    'password': 'password-here',
}

r = requests.post(url, data=data)
print(r.status_code)
print(r.reason)
print(r.content)

# At this endpoint, you obtain token
```


##### Send email endpoint (/)
```sh
import requests

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
```
### Technologies
- Django
- Django Rest Framework
- [Djangoroku](https://pypi.org/project/djangoroku/)
- Heroku


### Todos

 - Write MORE Tests
 - More documenting
 - Add more functionalities depending on developer's requirements
 

License
----

MIT

