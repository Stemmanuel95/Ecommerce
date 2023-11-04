from flask import Flask
import mysql.connector
from routes import *

app = Flask(__name__)

db_configuration = {
    'host': 'localhost',
    'user': 'Emmanuel',
    'passwd': 'emmanuel_2022',
    'database': 'ecommerce'
}

conn = mysql.connector.connect(**db_configuration)

cursor = conn.cursor()


cursor.close()
conn.close()

if __name__ == '__main__':
    app.run(debug=True)
