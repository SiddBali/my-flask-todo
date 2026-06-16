from flask import Flask, render_template, request

app = Flask(__name__)

tasks = []

@app.route('/', methods=["GET","POST"])
def home():

    if request.method == "POST":
        task = request.form.get("task")

        tasks.append(task)

    return render_template("index.html", tasks=tasks )

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)