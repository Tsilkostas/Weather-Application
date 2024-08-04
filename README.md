Enter file# Weather Application

## Overview

Welcome to the Weather Application, a Django-based project designed to manage weather data efficiently. This application features a RESTful API that supports basic CRUD operations and is secured using JWT authentication. It runs within Docker containers and uses SQLite as its database.

## Features

- **RESTful API**: Perform CRUD operations on weather data.
- **JWT Authentication**: Secure your API endpoints with JSON Web Tokens.
- **Swagger UI**: Explore and test the API endpoints using Swagger.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)

## Installation

Follow these steps to get the application up and running:

### 1. Clone the Repository


git clone https://github.com/yourusername/weather-app.git
cd weather-app

### 2. Create a .env File
Copy the example environment file and edit it to set your environment variables:

cp .env.example .env
* Edit .env to include:

* SECRET_KEY='your-secret-key'
* DEBUG=True
* ALLOWED_HOSTS='127.0.0.1,localhost,0.0.0.0'
* DATABASE_URL='sqlite:///db.sqlite3'

### 3. Build and Run the Application
Use Docker Compose to build and start the application:

docker-compose up --build.

This command builds the Docker images and starts the containers as specified in the docker-compose.yml file.

### 4. Apply Migrations
Open a new terminal and run the following command to apply database migrations:
docker-compose exec web python manage.py migrate

### 5. Access the Application
The application should now be running at http://127.0.0.1:8000/. You can access the Swagger UI at http://127.0.0.1:8000/swagger/ to explore the API endpoints.

### 6. Stopping the Application
To stop the application, use:

docker-compose down

### Static Files
In Django projects, static files (CSS, JavaScript, images) are collected into a single directory for easier management and serving in production.

To collect static files, run:

python manage.py collectstatic
This command gathers all static files into the directory specified by the STATIC_ROOT setting in your settings.py. contents here
