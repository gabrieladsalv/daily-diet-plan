# Daily Diet Plan API

## Overview

The [Project Name] API is a RESTful service designed for managing daily meal plans and diet tracking. It allows users to register, update, delete meals, and retrieve meal information. This API is built using Python and Flask framework, with SQLAlchemy for database management.

## Features

- **Register Meal**: Add a new meal with details such as name, description, type, date, time, and whether it's part of the diet.
- **Edit Meal**: Modify existing meal information, including all attributes.
- **Delete Meal**: Remove a meal from the database.
- **List Meals**: Retrieve a list of all meals for a user.
- **View Meal**: Get detailed information about a specific meal.

## Technologies Used

- Python
- Flask
- SQLAlchemy
- MySQL
- RESTful principles

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone [repository-url]
   cd [project-directory]
    ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the database:**
    - Create a MySQL database and update the connection string in `config.py`.
    - Run the following commands to create the tables:
      ```bash
      python manage.py db init
      python manage.py db migrate
      python manage.py db upgrade
      ```

4. **Run the application:**
    ```bash
    python app.py
    ```
    The API will be available at `http://localhost:3006`.


## API Endpoints

- **Register Meal**
  - URL: `/meals`
  - Method: `POST`
  - Request Body:
    ```json
    {
      "name": "Breakfast",
      "description": "Scrambled eggs with toast",
      "type": "Breakfast",
      "date": "2021-09-01",
      "time": "08:00",
      "is_diet": true
    }
    ```
  - Response:
    ```json
    {
      "id": 1,
      "name": "Breakfast",
      "description": "Scrambled eggs with toast",
      "type": "Breakfast",
      "date": "2021-09-01",
      "time": "08:00",
      "is_diet": true
    }
    ```
- **Edit Meal**
    - URL: `/meals/<meal_id>`
    - Method: `PUT`
    - Request Body:
        ```json
        {
        "name": "Lunch",
        "description": "Chicken salad with avocado",
        "type": "Lunch",
        "date": "2021-09-01",
        "time": "12:00",
        "is_diet": true
        }
        ```
    - Response:
        ```json
        {
        "id": 1,
        "name": "Lunch",
        "description": "Chicken salad with avocado",
        "type": "Lunch",
        "date": "2021-09-01",
        "time": "12:00",
        "is_diet": true
        }
        ```
- **Delete Meal**
    - URL: `/meals/<meal_id>`
    - Method: `DELETE`
    - Response:
        ```json
        {
        "message": "Meal deleted successfully"
        }
        ```
- **List Meals**

    - URL: `/meals`
    - Method: `GET`
    - Response:
        ```json
        [
        {
        "id": 1,
        "name": "Breakfast",
        "description": "Scrambled eggs with toast",
        "type": "Breakfast",
        "date": "2021-09-01",
        "time": "08:00",
        "is_diet": true
        },
        {
        "id": 2,
        "name": "Lunch",
        "description": "Chicken salad with avocado",
        "type": "Lunch",
        "date": "2021-09-01",
        "time": "12:00",
        "is_diet": true
        }
        ]
        ```

- **View Meal**

    - URL: `/meals/<meal_id>`
    - Method: `GET`
    - Response:
        ```json
        {
        "id": 1,
        "name": "Breakfast",
        "description": "Scrambled eggs with toast",
        "type": "Breakfast",
        "date": "2021-09-01",
        "time": "08:00",
        "is_diet": true
        }
        ```
## Author

- Gabriela Alvarenga

## Contact

For any questions, please contact me at [linkedin](https://www.linkedin.com/in/gabrieladsalvarenga/) or at [email](gabrielasalvarenga2@gmail.com).
