#!/bin/bash

# Run the Python script using the relative path to wsgi.py and set the working directory
gunicorn -w 1 -b 0.0.0.0:3001 --access-logfile - --chdir server wsgi:app
