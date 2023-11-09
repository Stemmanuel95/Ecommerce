#!/usr/bin/python3
"""Creating my database instance
for the ecommerce application"""

#from flask import Flask
from app import app
from flask_mysqldb import MySQL


# app.config['MYSQL_DATABASE_USER'] = 'Emmanuel'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'emmanuel_2022'
# app.config['MYSQL_DATABASE_DB'] = 'ecommerce'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL(app)

cursor = mysql.connection.cursor()

# Creating my primary database tables for the ecommerce application

create_users_table = """CREATE TABLE IF NOT EXISTS Users (
                 User_id INT AUTO_INCREMENT PRIMARY KEY,
                 User_name VARCHAR(255) NOT NULL,
                 Password VARCHAR(255) NOT NULL,
                 Email VARCHAR(255) NOT NULL,
                 Country VARCHAR(255),
                 City VARCHAR(255),
                 First_name VARCHAR(255),
                 Last_name VARCHAR(255),
                 Phone_number VARCHAR(20),
                 Profile_picture BLOB,
                 Address VARCHAR(255)
                 )
                 """

create_products_table = """CREATE TABLE IF NOT EXISTS Products (
                 Product_id INT AUTO_INCREMENT PRIMARY KEY,
                 Product_name VARCHAR(255) NOT NULL,
                 Price DECIMAL (10,2) NOT NULL,
                 Category VARCHAR(255),
                 Description VARCHAR(255),
                 Image_url VARCHAR(255),
                 Stock_quantity INT,
                 Manufacturer VARCHAR(100)
                 )
                 """

create_orders_table = """CREATE TABLE IF NOT EXISTS Orders (
                 Order_id INT AUTO_INCREMENT PRIMARY KEY,
                 User_id INT,
                 Product_id INT,
                 Quantity INT,
                 Total_price DECIMAL (10,2) NOT NULL
                 )
                 """

# executing the queries created above

cursor.execute(create_users_table)
cursor.execute(create_products_table)
cursor.execute(create_orders_table)

mysql.connection.commit()

cursor.close()


