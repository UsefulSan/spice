![Python](https://img.shields.io/badge/-Python-05122A?style=flat&logo=python)&nbsp;
![Django](https://img.shields.io/badge/-Django-05122A?style=flat&logo=django&logoColor=092E20)&nbsp;
![Docker](https://img.shields.io/badge/-Docker-05122A?style=flat&logo=Docker)&nbsp;
![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-05122A?style=flat&logo=PostgreSQL)&nbsp;
![HTML](https://img.shields.io/badge/-HTML-05122A?style=flat&logo=HTML5)&nbsp;
![JavaScript](https://img.shields.io/badge/-JavaScript-05122A?style=flat&logo=javascript)&nbsp;
![celery](https://img.shields.io/badge/-celery-05122A?style=flat&logo=celery)&nbsp;
![redis](https://img.shields.io/badge/-redis-05122A?style=flat&logo=redis)

## *SPICE HARVESTER*
Приложение, прогнозирующее будущую котировку валюты


### Для запуска приложения:

 - клонировать репозиторий `git clone https://github.com/universetoday/spice.git`
 - добавить python интерпретатор 
 - установить зависимости `pip freeze > requirements.txt`
 - создать БД PostgreSQL с именем `spice.db`
 - накатить миграции `py manage.py migrate`
 - запустить задачу в `core\tasks.py`
 - запустить `py manage.py runserver`
