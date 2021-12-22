# CR_python1

Реализовать простой сервис, который принимает и отвечает на HTTP-запросы
###Запуск в dev-окружении
Запуск develop-сервера

`docker-compose up`

Инициализация базы данных(применение миграций)

`docker-compose exec web python3 manage.py migrate`

Создание суперпользователя:

`docker-compose exec web python3 manage.py createsuperuser`

Для того чтобы авторизоваться нужно зайти на http://localhost:8000/admin

API находится на http://localhost:8000/api

Создание фейковых данных:

`docker-compose exec web python3 manage.py createmockdata`

###Описание
####Функциональность
* Получение всех городов из базы данных (использовать mock-данные)
* Получение всех улиц города из базы данных (использовать mock-данные)
* Создать магазин с данными о городе, улице, графике работы (по дням и по часам) и примечание
* Получить магазин/(-ы) на основе фильтрации по одному или нескольким аттрибутов у сущности магазина (см. предыдущий пункт)

####Инструменты
* Python 3.6+
* Django 2.2+
* Django REST Framework 
* Реляционная база данных (желательно – PostgreSQL)


####Условия
* Наличие README.md для описания проекта и способа его установки/запуска локально
* Работа с Docker будет большим плюсом
* Обратить внимание на проектирование таблиц базы данных. Вероятно, здесь будет не одна таблица и будут применимы внешние ключи (Foreign Key).

### 

[http://localhost:8000/admin]: http://localhost:8000/admin