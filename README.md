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


## API Endpoints

General Configuration

The project defines URL paths for core parts of the system, including routes for user management, planetarium resources, the admin panel, and auto-generated OpenAPI documentation.

Main Endpoints

### Admin Interface

	•	GET /admin/ - Django admin panel for managing data and users.

### API Documentation

	•	GET /api/schema/ - Automatically generated OpenAPI schema.
	•	GET /api/schema/swagger-ui/ - Swagger UI interface for viewing and testing the API.
	•	GET /api/schema/redoc/ - ReDoc interface for viewing the API.

### Users

Endpoints for user registration, authentication, and profile management:

	•	POST /api/v1/register/ - Register a new user.
	•	POST /api/v1/token/ - Obtain a JWT token for authentication.
	•	POST /api/v1/token/refresh/ - Refresh an existing JWT token.
	•	POST /api/v1/token/verify/ - Verify a JWT token.
	•	POST /api/token/blacklist/ - Add tokens to the blacklist to revoke access.
	•	GET /api/v1/me/ - View or update the profile of the authenticated user.

### Planetarium

Endpoints for managing shows, themes, domes, sessions, reservations, and tickets in the planetarium:

	•	GET /api/v1/planetarium/astronomy_show/ - Retrieve a list of astronomy shows.
	•	POST /api/v1/planetarium/astronomy_show/ - Create a new astronomy show.
	•	GET /api/v1/planetarium/show_theme/ - View available show themes.
	•	POST /api/v1/planetarium/show_theme/ - Add a new show theme.
	•	GET /api/v1/planetarium/planetarium_dome/ - View the list of available planetarium domes.
	•	POST /api/v1/planetarium/planetarium_dome/ - Add a new dome.
	•	GET /api/v1/planetarium/show_session/ - View available show sessions.
	•	POST /api/v1/planetarium/show_session/ - Create a new show session.
	•	GET /api/v1/planetarium/reservation/ - View reservations.
	•	POST /api/v1/planetarium/reservation/ - Create a reservation.
	•	GET /api/v1/planetarium/ticket/ - View available tickets.
	•	POST /api/v1/planetarium/ticket/ - Create a new ticket.

## Models app


<img width="523" alt="Знімок екрана 2024-11-01 о 15 23 08" src="https://github.com/user-attachments/assets/f339cb16-939d-4b63-9dc0-cf23b55603f0">


## App view

<img width="1333" alt="image" src="https://github.com/user-attachments/assets/97592083-eb0b-41bf-963f-19cac6b06129">



