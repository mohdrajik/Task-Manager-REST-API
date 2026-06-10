from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Razikshaikh@098'
app.config['MYSQL_DB'] = 'task_manager'

mysql = MySQL(app)

# Get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tasks")
    tasks = cur.fetchall()
    cur.close()

    result = []
    for task in tasks:
        result.append({
            "id": task[0],
            "title": task[1],
            "description": task[2],
            "status": task[3]
        })

    return jsonify(result)

# Get task by id
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tasks WHERE id=%s", (id,))
    task = cur.fetchone()
    cur.close()

    if task:
        return jsonify({
            "id": task[0],
            "title": task[1],
            "description": task[2],
            "status": task[3]
        })

    return jsonify({"message": "Task not found"}), 404

# Create task
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()

    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO tasks(title, description, status) VALUES(%s,%s,%s)",
        (
            data['title'],
            data['description'],
            data.get('status', 'Pending')
        )
    )

    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "Task created successfully"}), 201

# Update task
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.get_json()

    cur = mysql.connection.cursor()
    cur.execute(
        """
        UPDATE tasks
        SET title=%s,
            description=%s,
            status=%s
        WHERE id=%s
        """,
        (
            data['title'],
            data['description'],
            data['status'],
            id
        )
    )

    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "Task updated successfully"})

# Delete task
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM tasks WHERE id=%s", (id,))
    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "Task deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)