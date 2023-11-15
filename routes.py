from flask import request, render_template, url_for, redirect, session
from app import app, mysql

"""Route to the main home page"""
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

"""Route to the registration page for users"""
@app.route('/registration', methods=['GET', 'POST'])
def registration():
    #checking if the client is signing up
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        cursor = mysql.connection.cursor()

        # Inserting users details into the database
        cursor.execute("INSERT INTO Users (User_name, Email, Password) VALUES (%s, %s, %s)",
                       (name, email, password))
        mysql.connection.commit()

        cursor.close()

        #afterwards directing the user to the login page
        return redirect(url_for('login'))
    
    return render_template('registration.html')

#Route for the path where a user can contact the site admins
@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')

#Path to the products tab of the html page
@app.route('/Products')
def products():
    return render_template('product_list.html')

#Path to cart page
@app.route('/Cart')
def cart():
    return render_template('cart.html')

#Account login page
@app.route('/Account')
def account():
    return render_template('login.html')

#Logout page
@app.route('/Logout')
def logout():
    return render_template('logout.html')

"""Checking if user details exist and allowing already existing clients to login"""
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor = mysql.connection.cursor()

        # Check if the user exists
        cursor.execute("SELECT * FROM Users WHERE Email = %s AND Password = %s", (email, password))
        user = cursor.fetchone()

        if user:
            # Store user information in the session
            session['user_id'] = user['User_id']
            session['user_name'] = user['User_name']

            cursor.close()

            return redirect(url_for('account'))

        cursor.close()

    return render_template('login.html')