from flask import Flask, request, jsonify, render_template
import mysql.connector

db_configuration = {
    host="localhost",
    user="root",
    passwd='welcome1', 
    database='ecommerce'
}

conn = mysql.connector.connect(**db_configuration)

cursor = conn.cursor()

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login')
def home():
    return render_template('login.html')


cursor.close()
conn.close()