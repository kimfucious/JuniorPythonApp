FROM python:3.9

WORKDIR /app

RUN apt-get update && apt-get install -y nginx
RUN apt-get install -y redis-server
RUN apt-get install -y default-mysql-client

COPY nginx.conf /etc/nginx/sites-available/default

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENV DATA_BACKEND=redis

CMD if [ "$DATA_BACKEND" = "mysql" ]; \
    then \
        # Start MySQL service (modify the connection details accordingly)
        service mysql start && \
        python init_mysql.py && \
        gunicorn server:app -b 0.0.0.0:8000 -w 4; \
    else \
        # Start Redis service
        service redis-server start && \
        gunicorn server:app -b 0.0.0.0:8000 -w 4; \
    fi
