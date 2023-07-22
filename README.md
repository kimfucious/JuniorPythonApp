# The [enter adjective here] App

My kid asked me, "What's an API?" the other day, so I'm using this to teach him.

We're doing this in Python, because that's what he's learning in school.

## What's an API?

An API is a thing that you can ask something of and it might answer.

### APIs used in this app

-   [icanhazdadjoke](https://icanhazdadjoke.com/)
-   [The Yo Momma Joke API](https://yomomma.info/)
-   A custom API built with Flask (for the Wish List)

### Required External Python Dependencies

-   [art](https://pypi.org/project/art/)
-   [cowsay](https://pypi.org/project/cowsay/)
-   [halo](https://pypi.org/project/halo/)
-   [python-dotenv](https://pypi.org/project/python-dotenv/)
-   [requests](https://pypi.org/project/requests/)
-   [termcolor](https://pypi.org/project/termcolor/)

These can be installed with:

```shell
pip install -r requirements.txt
```

> **NOTE:** The backend server has its own dependencies. Read the `README.md` file there.

## Running the App

Use this command to run in the terminal:

```shell
python main.py
```

### Using Docker

It doesn't really make sense to Docker here, but it's here for demonstration purposes.

Build the app with this command:

```shell
docker build -t my-python-app .
```

Run the app interactively with:

```shell
docker run -it my-python-app
```

#### Using Docker Compose

This is a bit clunky. It's better to run locally or use Docker w/o compose in this scenario, but it's here for demonstrative purposes.

Build the app with:

```shell
docker compose build
```

Run the app (and backend) with:

```shell
docker-compose up -d
```

> **NOTE:** Be sure to use the dash here. The `-d` starts the services in detached mode, so that the interactive app does not get intermixed with the logging.

Run the following command to get the container id of the `my-python-app`:

```shell
docker ps
```

The id will look something like this: eeb58d36221d

Run the following command to attach to the container:

```shell
docker attach eeb58d36221d # <-- use the appropriate container id here
```

The rest is buggy, and I haven't figured it out yet. In short, the app does not show the initial screen. It's blank and when you press any key, it shows an error from the apps menu system. Press another key and you're in.

## Things to learn

-   ASCII art
-   Colorizing output
-   Docker
-   Environment variables
-   Enums
-   Error handling
-   Global variables
-   Interactive menus
-   Making HTTP calls to a RESTful API
-   Serializing JSON
-   Spinners
-   Using packages
