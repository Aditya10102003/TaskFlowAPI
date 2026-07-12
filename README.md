# TaskFlow API

A Full-Stack Task Management REST API built using **Django REST Framework** with **JWT Authentication**. The project allows users to register, log in, and securely manage their personal tasks with full CRUD operations and filtering.

---

## Features

- User Registration
- JWT Authentication (Login)
- Create Tasks
- View Tasks
- Update Tasks
- Delete Tasks
- Filter Tasks by Status and Priority
- SQLite Database
- Unit Testing using Django APITestCase

---

## Tech Stack

- Python
- Django
- Django REST Framework
- Simple JWT
- SQLite
- Git & GitHub
- Postman (API Testing)

---

## Installation

### Clone the repository

```bash
git clone https://github.com/Aditya10102003/TaskFlowAPI.git
```

### Move into the project

```bash
cd TaskFlowAPI
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py migrate
```

### Run Server

```bash
python manage.py runserver
```

Server runs at:

```
http://127.0.0.1:8000/
```

---

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/api/register/` | Register User |
| POST | `/api/login/` | Login and Receive JWT |

### Tasks

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/api/tasks/` | List Tasks |
| POST | `/api/tasks/` | Create Task |
| GET | `/api/tasks/<id>/` | Retrieve Task |
| PUT | `/api/tasks/<id>/` | Update Task |
| PATCH | `/api/tasks/<id>/` | Partial Update |
| DELETE | `/api/tasks/<id>/` | Delete Task |

### Filtering

```http
GET /api/tasks/?status=Pending
```

```http
GET /api/tasks/?priority=High
```

```http
GET /api/tasks/?status=Pending&priority=High
```

---

## Running Tests

```bash
python manage.py test
```

Example Output

```text
Found 5 test(s).

.....
----------------------------------------------------------------------
Ran 5 tests

OK
```

---

## Project Structure

```
TaskFlowAPI/
│
├── config/
├── tasks/
├── users/
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Author

**Aditya Yadav**

GitHub:
https://github.com/Aditya10102003