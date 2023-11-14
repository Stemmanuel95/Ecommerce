from flask import request, render_template, url_for, redirect
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')

@app.route('/Products')
def products():
    return render_template('product_list.html')

@app.route('/Cart')
def cart():
    return render_template('cart.html')

@app.route('/Account')
def account():
    return render_template('login.html')

@app.route('/Logout')
def logout():
    return render_template('logout.html')