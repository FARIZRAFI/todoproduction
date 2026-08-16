import os

MYSQL_HOST = os.getenv("MYSQL_HOST", "mysql")
MYSQL_PORT = int(os.getenv("MYSQL_PORT", "3306"))
MYSQL_USER = os.getenv("MYSQL_USER", "todo_user")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "todo_password")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "todo_db")

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
