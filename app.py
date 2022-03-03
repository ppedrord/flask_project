from flask import Flask, render_template, redirect, request, flash
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
app.secret_key = "ppedrord"

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TSL": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.getenv("EMAIL"),
    "MAIL_PASSWORD": os.getenv("PASSWORD")
    }

app.config.update(mail_settings)
mail = Mail(app)


class Contact:
    def __init__(self, name, email, message):
        self.name = name
        self.email = email
        self.message = message


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/send', methods=["GET", "POST"])
def send():
    if request.method == "POST":
        formContact = Contact(
            request.form["name"],
            request.form["email"],
            request.form["message"]
            )
        msg = Message(
            subject = f"Contact from Responsive Portfolio - {formContact.name}",
            sender = app.config.get("MAIL_USERNAME"),
            recipients = ["pedropaulommb@gmail.com", app.config.get("MAIL_USERNAME")],
            body = f"""
            
            {formContact.name} with the e-mail {formContact.email} sent you this message:
            
            {formContact.message}
            
            """
            )

        mail.send(msg)
        flash("Message sent successfully!")

    return redirect("/")


@app.route("/contacts")
def route_contact():
    return render_template("contacts.html")


@app.route("/user/<username>")
def route_user(username):
    return render_template("users.html", username=username)


@app.route("/portfolio/fixtures")
def route_fixtures():
    return render_template("fixtures.html")


if __name__ == "__main__":
    app.run(debug=True)
