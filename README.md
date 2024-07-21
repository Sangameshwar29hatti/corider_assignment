Flask CRUD Application with MongoDB

This is a Flask application that performs CRUD (Create, Read, Update, Delete) operations on a MongoDB database for a User resource using a REST API. The application is Dockerized for ease of deployment.

Requirements

Python 3.8+
Docker
Docker Compose

git clone https://github.com/Sangameshwar29hatti/corider_assignment.git
cd flask_app

Installing Dependencies
Install the required Python packages:

pip install -r requirements.txt

Running the Application
Using Docker
Build and run the Docker containers:

docker-compose up --build

Without Docker

python run.py

the project structure should be exact like this


Assignment
├── app/
│   ├── __init__.py
│   ├── models/
│   │   └── user.py
│   ├── schemas/
│   │   └── user.py
│   ├── services/
│   │   └── user_service.py
│   ├── controllers/
│   │   └── user_controller.py
│   ├── config.py
│   └── extensions.py
├── Dockerfile
├── requirements.txt
├── docker-compose.yml
├── run.py
└── README.md


docker-compose.yml

version: '3.8'

services:
  app:
    build: .
    ports:
      - "5000:5000"
    environment:
      MONGO_URI: "mongodb://mongo:27017/flask_db"
    depends_on:
      - mongo

  mongo:
    image: mongo
    ports:
      - "27017:27017"


License
This project is licensed under the MIT License.


This `README.md` file provides a comprehensive guide on setting up, running, and testing the Flask application, as well as an overview of the project structure and Docker setup. Make sure to replace `<repository-url>` with the actual URL of your GitHub repository.






