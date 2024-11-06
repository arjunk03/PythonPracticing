from flask import Flask, render_template, redirect, url_for, flash
from logging import DEBUG, INFO
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.logger.setLevel(INFO)

# Genereated using os.urandom(8) function call
app.secret_key = b"i\xb5\xbf1D\x9fX\xd7"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////site.db"

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)


@app.route("/")
def home():
    app.logger.info("home method called")
    return render_template("home.html")


@app.route("/test")
def test():
    app.logger.info("test method called")
    return render_template("test.html")


@app.route("/test2")
def test2():
    app.logger.info("test2 method called")
    flash("Redirecting the request from test2 to test")
    return redirect(url_for("test"))


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("registration.html", title="Register", form=form)


@app.route("/login")
def login():
    form = LoginForm()
    if form.validate_on_submit():
        app.logger.info("User :" + form.email.data + " is logged in")
        flash("Acount created")
        return redirect(url_for("home"))

    if form.errors:
        flash("validation errors: ", str(form.errors))
        app.logger.error("validation error: \n" + str(form.erros))

    return render_template("login.html", title="Login", form=form)


@app.errorhandler(404)
def page_not_found(e):
    app.logger.info("error 404 method called")
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, port=8182)
