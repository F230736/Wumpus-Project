from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder="../")

@app.route("/")
def home():
    return send_from_directory("../", "index.html")

@app.route("/test")
def test():
    return {"message": "Vercel deployment working"}