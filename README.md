# Task Manager REST API

A professional RESTful API built using Python, Flask, and MySQL for managing tasks efficiently. This project demonstrates full CRUD operations with clean API design and JSON-based responses.

---

## 🚀 Features

* Create new tasks
* Retrieve all tasks
* Retrieve task by ID
* Update existing tasks
* Delete tasks
* MySQL database integration
* RESTful API architecture
* JSON response format

---

## 🛠️ Tech Stack

* Python
* Flask
* Flask-MySQLdb
* MySQL
* Thunder Client (API Testing)

---

## 📁 Project Structure

```
Task-Manager-REST-API/
│
├── app.py
├── README.md
└── screenshots/
    ├── create_task.png
    ├── get_tasks.png
    ├── update_task.png
    └── delete_task.png
```

---

## 🗄️ Database Setup

Create database and table using MySQL:

```sql
CREATE DATABASE task_manager;

USE task_manager;

CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(20) DEFAULT 'Pending'
);
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/mohdrajik/Task-Manager-REST-API.git
cd Task-Manager-REST-API
```

---

### 2. Install Dependencies

```bash
pip install flask flask-mysqldb
```

---

### 3. Configure Database

Update your MySQL credentials in `app.py`:

```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'YOUR_PASSWORD'
app.config['MYSQL_DB'] = 'task_manager'
```

---

### 4. Run Application

```bash
python app.py
```

Server will run at:

```
http://127.0.0.1:5000
```

---

## 📌 API Endpoints

| Method | Endpoint    | Description          |
| ------ | ----------- | -------------------- |
| GET    | /tasks      | Get all tasks        |
| GET    | /tasks/<id> | Get task by ID       |
| POST   | /tasks      | Create new task      |
| PUT    | /tasks/<id> | Update existing task |
| DELETE | /tasks/<id> | Delete task          |

---

## 🧪 API Testing

Test all APIs using:

* Thunder Client (VS Code)
* Postman

---

## 📸 Screenshots

### ➕ Create Task

*Add screenshot here*

### 📋 Get Tasks

*Add screenshot here*

### ✏️ Update Task

*Add screenshot here*

### ❌ Delete Task

*Add screenshot here*

---

## 📈 Future Improvements

* JWT Authentication
* User Login System
* Pagination
* Search & Filtering
* Deployment on cloud (Render / Railway)

---

## 👨‍💻 Author

**Razik Shaikh**
Python Developer | Flask | MySQL | REST API

---

## ⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub!
