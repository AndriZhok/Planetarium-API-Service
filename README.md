# Planetarium-API-Service
Do you like learning new things about stars and planets? If so - this project is 100% for you. Make visitors happy to book tickets online for their favourite ShowSessions in local Planetarium.

## Installing using GitHub

Install PostgresSQL and create db

```
git clone [https: //github.com/Y-Havryliv/cinema-API.git](https://github.com/AndriZhok/Planetarium-API-Service.git)
cd Planetarium-API-Service
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
set DB_HOST=<your db hostname>
set DB_NAME=<your db name>
set DB_USER=<your db username>
set DB_PASSWORD=<your
db user password>
set SECRET_KEY=<your secret key>
python manage.py migrate
python manage.py runserver
```

## Run with docker

Docker should be installed

```
docker-compose build
docker-compose up
```

## Getting access

• create user via /api/v1/register/
• get access token via /api/v1/token/

## OR

Login like admin

```
Email: admin123@gmail.com
Password: admin
```


## Features


• JWT authenticated
• Admin panel /admin/
• Documentation is located at /api/doc/swagger/
• Managing reservations and tickets
• Creating astronomy show with theme
• Creating planetarium dome
• Adding show session


