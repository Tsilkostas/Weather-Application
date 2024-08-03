Weather Application
Overview
This is a weather application built with Django and Docker. It provides a RESTful API for managing weather data, including basic CRUD operations. The application is configured with JWT authentication for secure access and uses SQLite for its database.

Features
RESTful API: Perform CRUD operations on weather data.
JWT Authentication: Secure your API endpoints with JSON Web Tokens.
Swagger UI: Easily explore and test the API using Swagger.

Prerequisites
Docker
Docker Compose

Installation
Follow these steps to get the application up and running:

1. Clone the Repository:
git clone https://github.com/yourusername/weather-app.git
cd weather-app
2. Create a .env File:
cp .env.example .env
Edit .env to set your environment variables. Example:
SECRET_KEY='your-secret-key'
DEBUG=True
ALLOWED_HOSTS='127.0.0.1,localhost,0.0.0.0'
DATABASE_URL='sqlite:///db.sqlite3'
3. Build and Run the Application:
Use Docker Compose to build and start the application:
docker-compose up --build
This command builds the Docker images and starts the containers as specified in the docker-compose.yml file.
4. Apply Migrations
Open a new terminal and run the following command to apply database migrations:
docker-compose exec web python manage.py migrate
5. Access the Application
The application should now be running at http://127.0.0.1:8000/. You can access the Swagger UI at http://127.0.0.1:8000/swagger/ to explore the API endpoints.
6. Stopping the Application:
To stop the application, use:
docker-compose down
