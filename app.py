from flask import Flask, flash, redirect, render_template, request, redirect, url_for

app = Flask(__name__)

##db =

@app.route('/', methods = ["GET", "POST"])
def index():
    return render_template('index.html')