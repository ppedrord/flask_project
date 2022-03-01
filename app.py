from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contacts")
def route_contact():
    return render_template("contacts.html")


@app.route("/user/<username>")
def route_user(username):
    return render_template("users.html", username=username)

@app.route("/fixtures")
def route_fixtures():
    return render_template("fixtures.html")


if __name__ == "__main__":
    app.run(debug=True)
