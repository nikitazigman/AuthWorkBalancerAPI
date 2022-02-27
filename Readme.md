# TEST setup

Here is a test setup to figure out how to do an authorization via nginx using an extarnal Auth web service.

## setup  

the project contains two django web services: auth_service and resource_service.
The auth_service emulates token creation and token validation requests (login and token respectevly).

The resource_service emulates content service, which client request providing the given token from the auth_service.

Nginx is setted up the following way:

- It redirects to login and registration with out the authorizatinon.
- It request token validation before to route to the content.

## how to run

to run just type:

    docker-compose up -d --build