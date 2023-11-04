from flask import request, render_template, url_for, redirect

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login')
def home():
    return render_template('login.html')