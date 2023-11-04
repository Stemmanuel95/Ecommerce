from flask import Flask
import mysql.connector

app = Flask(__name__)

db_configuration = {
    'host': 'localhost',
    'user': 'Emmanuel',
    'passwd': 'emmanuel_2022',
    'database': 'ecommerce'
}

conn = mysql.connector.connect(**db_configuration)

cursor = conn.cursor()

from routes import *

if __name__ == '__main__':
    app.run(debug=True)

# cursor.close()
# conn.close()


