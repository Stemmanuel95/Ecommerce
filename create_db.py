#!/usr/bin/python3
"""Creating my database instance
for the ecommerce application"""

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd='welcome1',
    database='ecommerce'
)

mycursor = mydb.cursor()

# Creating my primary database tables for the ecommerce application

mycursor.execute("""CREATE TABLE IF NOT EXISTS Users (
                 User_id INT AUTO_INCREMENT PRIMARY KEY,
                 User_name VARCHAR(255) NOT NULL,
                 Password VARCHAR(255) NOT NULL,
                 Email VARCHAR(255) NOT NULL,
                 Country VARCHAR(255),
                 City VARCHAR(255)
                 )
                 """)

mycursor.execute("""CREATE TABLE IF NOT EXISTS Products (
                 Product_id INT AUTO_INCREMENT PRIMARY KEY,
                 Product_name VARCHAR(255) NOT NULL,
                 Price DECIMAL (10,2) NOT NULL,
                 Category VARCHAR(255)
                 )
                 """)

mycursor.execute("""CREATE TABLE IF NOT EXISTS Orders (
                 Order_id INT AUTO_INCREMENT PRIMARY KEY,
                 User_id INT,
                 Product_id INT,
                 Quantity INT,
                 Total_price DECIMAL (10,2) NOT NULL
                 )
                 """)

# mycursor.execute("SHOW DATABASES")

mycursor.close()
mydb.close()
