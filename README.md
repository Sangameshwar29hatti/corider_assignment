# Flask Application for CRUD Operations on MongoDB

## Overview

This project is a Flask application that performs CRUD (Create, Read, Update, Delete) operations on a MongoDB database for a User resource. The application is designed to demonstrate best practices in Flask and Docker containerization.

## Project Structure

The project is organized as follows:


flask_app/
├── app/
│ ├── init.py
│ ├── main/
│ │ ├── init.py
│ │ ├── routes.py
│ ├── models.py
│ ├── schemas.py
│ └── config.py
├── Dockerfile
├── requirements.txt
├── run.py
├── docker-compose.yml
└── README.md


- **`app/`**: Contains the main application code.
  - `__init__.py`: Initializes the Flask application and sets up the MongoDB connection.
  - `main/`:
    - `__init__.py`: Initializes the `main` module of the application.
    - `routes.py`: Defines API endpoints and route handling for CRUD operations.
  - `models.py`: Contains the data model for the User resource.
  - `schemas.py`: Defines schemas for data validation and serialization.
  - `config.py`: Configuration settings for the application.

- **`Dockerfile`**: Contains the instructions to build the Docker image for the Flask application.

- **`requirements.txt`**: Lists the Python packages required for the application.

- **`run.py`**: The entry point to start the Flask application.

- **`docker-compose.yml`**: Configures Docker services for the Flask application and MongoDB.

- **`README.md`**: This file.

## Setup and Installation

Install Dependencies
pip install -r requirements.txt


### Prerequisites

- **Python**: Ensure Python 3.x is installed.
- **Docker**: Ensure Docker and Docker Compose are installed.

### Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Sangameshwar29hatti/corider_flask_assignment.git
   cd corider_flask_assignment

## Running command

docker-compose up --build




