<h2 align="center">Ps4shop</h2>
<br/>


Ps4Shop - небольшой интернет-магазин для продажи дисков для ps4. Есть градация игр по категориям, жанрам, ограничениям 
по возрасту, студиям, популярным тегам. Так же реализована возможность зарегестрированным ползователям добавлять товар в 
корзину и оставлять отзывы под конкретным продуктом. Добавления товаров происходит через админ панель, так же управляются профили 
пользователей, есть возможность исправлять и удалять их комментарии.


![Python](https://img.shields.io/badge/-Python-black?style=flat-square&logo=Python)
![Django](https://img.shields.io/badge/-Django-0aad48?style=flat-square&logo=Django)
![Django Rest Framework](https://img.shields.io/badge/DRF-red?style=flat-square&logo=Django)
![Postgresql](https://img.shields.io/badge/-Postgresql-%232c3e50?style=flat-square&logo=Postgresql)
![Docker](https://img.shields.io/badge/-Docker-46a2f1?style=flat-square&logo=docker&logoColor=white)
![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github)
![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=flat-square&logo=telegram&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=flat-square&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=flat-square&logo=bootstrap&logoColor=white)
## Старт

#### 1) Скопировать репозиторий

##### 2) Установить Docker и docker-compose

#### 3) Создать образ
    docker-compose build

##### 4) Запустить контейнер

    docker-compose up

##### 5) Провести миграции

    docker-compose  exec web /bin/bash python manage.py migrate

##### 6) Создать администратора

    docker-compose  exec web /bin/bash python manage.py createsuperuser
##### 7) Управление сайтом происходит через админ-панель "http://localhost:1337/admin"

## Поддержка

По всем вопросам обращаться [swankyyy1@gmail.com](swankyyy1@gmail.com)