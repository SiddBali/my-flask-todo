from flask import Flask, jsonify, render_template, request, redirect
import mysql.connector
app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="Pass@3993",
        database="todo"
    )

con = get_db_connection()
cursor = con.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS task (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL
    )
    """
)
con.commit()
cursor.close()
con.close()

@app.route('/getTable', methods=["GET"])
def get_tables():
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute("SHOW TABLES;")
    data = cursor.fetchall()
    cursor.close()
    con.close()
    table_names=[table[0] for table in data]
    return jsonify({"tables": table_names}), 200




tasks = []

@app.route('/', methods=["GET", "POST"])
def home():

    if request.method == "POST":

        task = request.form.get("task")

        if task and task.strip():
            con = get_db_connection()
            cursor = con.cursor()
            query = "INSERT INTO task(title) VALUES(%s)"
            cursor.execute(query, (task,))
            con.commit()
            cursor.close()
            con.close()

    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM task")
    tasks = cursor.fetchall()
    cursor.close()
    con.close()

    return render_template(
        "index.html",
        tasks=tasks
    )


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_task(id):
    if request.method == "POST":
        updated_task = request.form.get("task")
        con = get_db_connection()
        cursor = con.cursor()
        query = """
        UPDATE task
        SET title=%s
        WHERE id=%s
        """
        cursor.execute(
            query,
            (updated_task, id)
        )
        con.commit()
        cursor.close()
        con.close()
        return redirect("/")

    con = get_db_connection()
    cursor = con.cursor()
    query = "SELECT * FROM task WHERE id=%s"
    cursor.execute(query, (id,))
    task = cursor.fetchone()
    cursor.close()
    con.close()

    return render_template(
        "edit.html",
        task=task
    )




















if __name__ == '__main__':
    app.run(debug=True)