from flask import Flask, render_template
from logging import DEBUG, INFO

app = Flask(__name__)
app.logger.setLevel(INFO)


@app.route("/")
def home():
    app.logger.info("home method called")
    return render_template("home.html")


@app.route("/test")
def test():
    app.logger.info("test method called")
    return render_template("test.html")


@app.errorhandler(404)
def page_not_found(e):
    app.logger.info("error 404 method called")
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, port=8182)
