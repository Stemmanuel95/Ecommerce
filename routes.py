from flask import request, render_template, url_for, redirect
from app import app

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login')
def home():
    return render_template('login.html')