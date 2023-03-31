# Склады и товары

## Описание

У нас есть продукты, которыми торгует компания. Продукты описываются названием и необязательным описанием 
(см. `models.py`). Также компания имеет ряд складов, на которых эти продукты хранятся. У продукта на складе
есть стоимость хранения, поэтому один и тот же продукт может иметь разные стоимости на разных складах.

Реализовано REST API для создания/получения/обновления/удаления продуктов и складов, поиск продуктов по 
названиям и описанию, поиск складов, в которых есть определенный продукт (по идентификатору).



## Quickstart

Для запуска проекта:

    git clone https://github.com/AlinaProkofeva/webpy_docker_01
    cd docker_1_2/stocks_products

    cp .env.template .env

В .env необходимо указать свои переменные окружения

Для запуска контейнера:

    docker build . --tag stocks_products 
    docker run --name stock_prod_01 -p 8001:8000 stocks_products

## URL для запросов

http://127.0.0.1:8001/api/v1/products/

http://127.0.0.1:8001/api/v1/stocks/

## Примеры запросов

* создание продукта

POST http://127.0.0.1:8001/api/v1/products/

    Content-Type: application/json

    {
    "title": "Помидор",
    "description": "Лучшие помидоры на рынке"
    }


* получение продуктов

GET http://127.0.0.1:8001/api/v1/products/

    Content-Type: application/json


* обновление продукта

PATCH http://127.0.0.1:8001/api/v1/products/1/

    Content-Type: application/json

    {
    "description": "Самые сочные и ароматные помидорки"
    }

* удаление продукта

DELETE http://127.0.0.1:8001/api/v1/products/1/

    Content-Type: application/json

* поиск продуктов по названию и описанию

GET http://127.0.0.1:8001/api/v1/products/?search=помид

    Content-Type: application/json

* создание склада

POST http://127.0.0.1:8001/api/v1/stocks/

    Content-Type: application/json

    {
    "address": "мой адрес не дом и не улица, мой адрес сегодня такой: www.ленинград-спб.ru3",
    "positions": [
        {
        "product": 1,
        "quantity": 250,
        "price": 120.50
        }
    ]
    }
