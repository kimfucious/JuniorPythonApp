# The Server

This is an API to serve as the backend for the Wishlist.

## Required External Dependencies

-   [Flask](https://pypi.org/project/Flask/)
-   [gunicorn](https://pypi.org/project/gunicorn/)
-   [redis (optional)](https://pypi.org/project/redis/)
-   [mysql-connector-python (optional)](https://pypi.org/project/mysql-connector-python/)

Install all deps with the below or install individually:

```shell
pip install -r requirements.txt
```

## Running the App

To run the server app, you need to:

1. Optionally start the Redis database or MySQL
2. Start the web/api server

These can be done manually, or using Docker compose [see here](#run-the-wsgi-server-in-a-docker-container).

> **NOTE:** The server can run with either an in memory list of wishes or with Redis or MySQl. This can be controlled by the `use_redis` variable and `use_mysql` in the `server.py` file, per the below.

```python
# Set (only) one of these to True, or both to False to use the wishes list
use_redis = False
use_mysql = False
data_access = DataAccess(use_redis, use_mysql)
```

> **NOTE:** I haven't got mysql working yet, so don't try to use it!

### Flask Dev Server

Flask has its own HTTP server, but it is not considered production ready, but is fine for development.

Run this command to start the dev server:

```shell
python3 server.py
```

The below code block in the `server.py` file runs the server on port 3001, which the app is configured to use. The `debug=True` parameter restarts the server on code changes in the `server.py` file.  You'd want to set this to False in prod.

```python
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001, debug=True)
```

### Run with WSGI Server

You can use [Gunicorn](https://gunicorn.org/) to run the app with this command from the `server` directory:

```shell
gunicorn -w 1 -b 0.0.0.0:3001 --access-logfile - wsgi:app
```

> **Note:** We are only using 1 worker here to maintain consistent data. In the Docker version, we run with 4 workers and use a Redis database to maintain data consistency.

As a convenience, you can execute the `start_gunicorn.sh` file from the project's root directory.

### Run the WSGI Server in a Docker container

The `server.py` file contains the following code at the bottom.

Use the `app.run` command appropriate for

```python
if __name__ == "__main__":
    # Use this when running in prod
    app.run(host="0.0.0.0", port=3001)
    # Use this when running in dev
    # app.run(host="0.0.0.0", port=3001, debug=True)
```

Build and run the docker image in a container with these commands:

```shell
docker compose build -t my_flask_app
docker compose up
```

Stop the app with `CTRL-C` and then this command to clean up:

```shell
docker compose down --name my_flask_app_container
```

## To Do

-   Add a version that uses a database
