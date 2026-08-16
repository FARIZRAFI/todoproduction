from flask import Flask, request, redirect, render_template
import mysql.connector
import redis
import os

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "mysql"),
        port=int(os.getenv("MYSQL_PORT", "3306")),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE")
    )

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", "6379"),
    ),
    decode_responses=True
)


@app.route("/")
def index():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM todos ORDER BY id DESC")
    todos = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template("index.html", todos=todos)


@app.route("/add", methods=["POST"])
def add_todo():
    title = request.form["title"]

    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO todos (title) VALUES (%s)",
        (title,)
    )

    db.commit()

    cursor.close()
    db.close()

    redis_client.delete("todos")

    return redirect("/")


@app.route("/delete/<int:todo_id>")
def delete_todo(todo_id):
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "DELETE FROM todos WHERE id = %s",
        (todo_id,)
    )

    db.commit()

    cursor.close()
    db.close()

    redis_client.delete("todos")

    return redirect("/")


@app.route("/health")
def health():
    return {
        "status": "healthy"
    }


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
