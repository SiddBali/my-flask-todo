from flask import Flask, jsonify, render_template, request, redirect
import mysql.connector
app = Flask(__name__)

con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pass@3993",
    database="todo"
)

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

@app.route('/getTable', methods=["GET"])
def get_tables():
    cursor = con.cursor()
    cursor.execute("SHOW TABLES;")
    data = cursor.fetchall()
    cursor.close()
    table_names=[table[0] for table in data]
    return jsonify({"tables": table_names}), 200




tasks = []

@app.route('/', methods=["GET", "POST"])
def home():

    if request.method == "POST":

        task = request.form.get("task")

        if task and task.strip():

            cursor = con.cursor()

            query = "INSERT INTO task(title) VALUES(%s)"

            cursor.execute(query, (task,))

            con.commit()

            cursor.close()

    cursor = con.cursor()

    cursor.execute("SELECT * FROM task")

    tasks = cursor.fetchall()

    cursor.close()

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

@app.route("/edit/<int:task:id>")
def edit_task(id):
    if request.method == "POST":

        updated_task = request.form.get("task")

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

        return redirect("/")

    cursor = con.cursor()

    query = "SELECT * FROM task WHERE id=%s"

    cursor.execute(query, (id,))

    task = cursor.fetchone()

    cursor.close()

    return render_template(
        "edit.html",
        task=task
    )




















if __name__ == '__main__':
    app.run(debug=True)