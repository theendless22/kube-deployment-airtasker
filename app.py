import os
from flask import Flask

app = Flask(__name__)
APP_NAME = os.getenv("APP_NAME", "airtasker")


@app.route("/")
def root():
    return APP_NAME, 200, {"Content-Type": "text/plain"}


@app.route("/healthcheck")
def healthcheck():
    return "OK", 200, {"Content-Type": "text/plain"}
