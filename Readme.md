# Inventory Management System API

## Overview

The Inventory Management System API allows businesses to efficiently manage their stock of products. This API provides endpoints for creating, reading, updating, and deleting (CRUD) inventory items. It uses JSON Web Tokens (JWT) for secure authentication.

## Features

- User registration and login
- JWT-based authentication
- CRUD operations for inventory items
- Secure access to the API

## Technologies Used

- Django
- Django REST Framework
- JWT Authentication
- PostgreSQL
- Python 3.x

## Installation

### Prerequisites

- Python 3.x installed on your machine.
- Virtualenv
- PostgreSQL.

### Steps to Set Up the Project

1. **Clone the Repository**

   git clone <repository-url>
   cd inventory_management_system

2. **Create a Virtual Environment**

   python -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`

3. **Install Required Packages**

   pip install -r requirements.txt

4. **create .env**

   configure django_secret(djano secreate), DEBUG(True), JWT_SECRET(jwt key) DB_MODE(dev or prod) \*\*note this all are variable names use same

   \*\*db configuration for development mode in env (DB_MODE="dev")
   DB_ENGINE(engine name), DB_NAME(database name), DB_USER(admin name), DB_PASSWORD(admin password), DB_HOST, DB_PORT \*\*note this all are variable names use same

   \*\*db configuration for production mode in env (DB_MODE="prod")
   PRO_DB_ENGINE(engine name), PRO_DB_NAME(database name), PRO_DB_USER(admin name), PRO_DB_PASSWORD(admin password), PRO_DB_HOST, DB_PORT \*\*note this all are variable names use same

5. **Run Migrations**

   python manage.py migrate

6. **runserver**
   cmd
   start.bat

**API Endpoints**

**_Authentication Endpoints_**

### Register a New User

URL: /api/auth/register/
Method: POST
Request Body:

json
{
"email": "user@example.com"
}

Response:
Success: 201 Created
json
{
"email": "user@example.com",
"password": "generated_password"
}

Error: 400 Bad Request
json
{
"error": "A user with this email already exists."
}

**\*Login User**
URL: /api/auth/login/
Method: POST
Request Body:
json
{
"email": "user@example.com",
"password": "your_password"
}

Response:
Success: 200 OK
json
{
"token": "jwt_token",
"refresh_token": "refresh_token",
"ok": "cookies stored!"
}

Error: 400 Bad Request
json
{
"error": "Invalid Email, please provide valid email"
}

**Logout User**
URL: /api/auth/logout/
Method: POST

Response:
Success: 200 OK
json
{
"message": "Logged out successfully."
}

### Inventory Endpoints

**Create Inventory Item**
URL: /api/mgmt/inventory/
Method: POST

Request Body:
json
{
"name": "Item Name",
"description": "Item Description"
}

Response:
Success: 201 Created
json
{
"message": "Inventory Created"
}

Error: 400 Bad Request
json
{
"error": "please provide the unique name & description"
}

**Get All Inventory Items**
URL: /api/mgmt/inventory/
Method: GET

Response:
Success: 200 OK
json
[
{
"id": "<uuid>",
"name": "Item Name",
"description": "Item Description"
},
...
]

**Get Inventory Item by ID**
URL: /api/mgmt/inventory/<uuid:pk>/
Method: GET
Response:
Success: 200 OK
json
{
"id": "<uuid>",
"name": "Item Name",
"description": "Item Description"
}

Error: 200 OK (if not found)
json
{
"message": "Inventory does't exists"
}

**Update Inventory Item**
URL: /api/mgmt/inventory/<uuid:pk>/
Method: PUT

Request Body:
json
{
"name": "Updated Item Name",
"description": "Updated Item Description"
}

Response:
Success: 200 OK
json
{
"message": "Inventory Updated"
}

**Delete Inventory Item**
URL: /api/mgmt/inventory/<uuid:pk>/
Method: DELETE
Response:
Success: 204 No Content

---````------------------:^

### Explaination 
Gdrive - https://drive.google.com/file/d/1YCdnRHgfcIs0u4Qvr1P9yCRM4idASNDp/view?usp=sharing
or
loom - https://www.loom.com/share/30482e0bcae54223abc8b3d553f53a5d?sid=897ccf2f-7358-4af2-9261-a3ac0a308a0d 

### For more information refer swagger documebtation

http://host:port/api/schema/swagger-ui/

Portfolio = https://asifrazvi.netlify.app/

----Thankyou :)
