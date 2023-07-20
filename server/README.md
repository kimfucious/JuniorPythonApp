# The Server

This is a flask API to serve as the backend for the Wishlist.

# Running the App

Flask has its own web server, but it is not considered production ready.

Run this command to start the server:

```shell
flask --app server run
```

Run this command to start the server in debug:

```shell
flask --app server --debug run
```

> Running in debug mode allows changes the server app to become active on save without having to restart the server.

## To Do

-   Implement [WSGI server](https://www.toptal.com/flask/flask-production-recipes#:~:text=Although%20Flask%20has%20a%20built,and%20proxying%20request%20with%20Nginx.)
-   Add a database
-   Dockerize the app
