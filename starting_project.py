from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/contacts")
def route_contact():
    return render_template("contacts.html")


@app.route("/user/<username>")
def route_user(username):
    return render_template("users.html", username=username)


if __name__ == "__main__":
    app.run(debug=True)
