from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == 'GET':
        return render_template("form.html")
    elif request.method == 'POST':
        print(request.form['name'], request.form['email'])
        return render_template("form.html")
