This project is a ToDo API built using FastAPI and SQLAlchemy. It provides endpoints to manage tasks in a ToDo list.

Features
CRUD Operations: Create, Read, Update, and Delete tasks.
Asynchronous: Utilizes FastAPI's async capabilities for high performance.
Database Integration: Uses SQLAlchemy ORM to interact with a SQLite database.

Installation

1. Clone the repository:
git clone https://github.com/ama-nana/Fastapi_todo.git
cd Fastapi_todo

2. Install dependencies:
pip install -r requirements.txt

3. Run the application:
uvicorn main:app --reload

The API will be available at http://localhost:8000/docs

API Documentation
Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc

Usage

1. Create a task:
POST /tasks/

2. Get all tasks:
GET /tasks/

3. Get a single task:
GET /tasks/{task_id}/

4. Update a task:
PUT /tasks/{task_id}/

5. Delete a task:
DELETE /tasks/{task_id}/

Contributing

Contributions are welcome! Fork the repository and submit a pull request with your changes.

License
This project is licensed under the MIT License - see the LICENSE file for details.

