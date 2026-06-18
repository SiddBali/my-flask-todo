from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Pass%3993@localhost/todo_app"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)


tasks = []

@app.route('/', methods=["GET","POST"])
def home():

    if request.method == "POST":
        task = request.form.get("task")
        new_task = Task(title=task)
        db.session.add(new_task)
        db.session.commit()
    return render_template("index.html", tasks=Task.query.all() )

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)