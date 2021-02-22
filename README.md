# UdictiMailer API


[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/maen08)

API that helps to send the multiple emails (currently, used only for UDICTI official projects). Easy to integrate in your project !



### INTRODUCTION

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


### ENDPOINTS

Endpoint | HTTP Method | Parameter | Description
| ------ | ------ | ------ | ------ |
| register/ | POST | `email`, `username`, `password` | Endpoint to register user. All parameters are required. Make sure you are using the same names even if in DOM (HTML elements eg. name="email")
| login/ | POST | `username`, `password` | Pass the same username and password which used to register a particular user. Any other different parameter will result an error. Successful logged in user will obtain `token`
| test/ |GET | NULL | This is the endpoint just to test your `token` and all setup if everything works fine. You must get `200 OK` response
| / | GET | `email-subject`, `email-body`, `email-receiver` | The endpoint that sends email. Pass the parameters required and the `token` to send emails.



### DATA TYPES OF PARAMETERS
- email `(String)` : Unique email per user
-  username `(String)` : Unique username per user
-   password `(String)` : Adviced to be strong password
-   email-subject `(String)`: The subject of email
-   email-body `(String)`: The body itself
-   email-receiver `(String)`: Receiver's emails. May be multiple emails separated by a comma (,)





### ENDPOINT TESTS
You can test the endpoints and HTTP requests using any tool (Postman, being so common) that you're comfortable with. This documentation uses `requests` to perform some of the methods, just to give an example.

```sh
$ cd dillinger
$ npm install -d
$ node app
```

For production environments...

```sh
$ npm install --production
$ NODE_ENV=production node app
```



### Development

Want to contribute? Great!

Dillinger uses Gulp + Webpack for fast developing.
Make a change in your file and instantaneously see your updates!

Open your favorite Terminal and run these commands.

First Tab:
```sh
$ node app
```

Second Tab:
```sh
$ gulp watch
```

(optional) Third:
```sh
$ karma test
```
#### Building for source
For production release:
```sh
$ gulp build --prod
```
Generating pre-built zip archives for distribution:
```sh
$ gulp build dist --prod
```
### Docker
Dillinger is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8080, so change this within the Dockerfile if necessary. When ready, simply use the Dockerfile to build the image.

```sh
cd dillinger
docker build -t joemccann/dillinger:${package.json.version} .
```
This will create the dillinger image and pull in the necessary dependencies. Be sure to swap out `${package.json.version}` with the actual version of Dillinger.

Once done, run the Docker image and map the port to whatever you wish on your host. In this example, we simply map port 8000 of the host to port 8080 of the Docker (or whatever port was exposed in the Dockerfile):

```sh
docker run -d -p 8000:8080 --restart="always" <youruser>/dillinger:${package.json.version}
```

Verify the deployment by navigating to your server address in your preferred browser.

```sh
127.0.0.1:8000
```



### Todos

 - Write MORE Tests
 - More documenting
 - Add more functionalities depending on developer's requirements
 

License
----

MIT

