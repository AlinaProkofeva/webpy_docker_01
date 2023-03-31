FROM python:3.11-slim

RUN mkdir code
WORKDIR code

ADD . /code/

RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate


CMD gunicorn stocks_products.wsgi:application -b 0.0.0.0:8000

