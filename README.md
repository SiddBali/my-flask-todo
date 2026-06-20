# Flask Todo App

A simple Flask-based todo application using MySQL for task storage.

## Features

- Add new tasks
- View all tasks
- Edit existing tasks
- Simple templates for home, about, contact, and edit views

## Requirements

- Python 3
- Flask
- mysql-connector-python
- MySQL server running locally

## Setup

1. Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

2. Start your MySQL server.
3. Ensure the `todo` database exists:

```bash
mysql -h 127.0.0.1 -u root -p
CREATE DATABASE IF NOT EXISTS todo;
```

4. Run the app:

```bash
python3 app.py
```

## Configuration

The database connection is configured in `app.py`:

```python
def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="Pass@3993",
        database="todo"
    )
```

Update these values if your MySQL credentials or host are different.

## GitHub

To add this file to your GitHub repository:

```bash
git add README.md
git commit -m "Add README"
git push
```
