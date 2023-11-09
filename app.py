from flask import Flask
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

with open('db.yaml','r') as config_file:
    db = yaml.safe_load(config_file)

#db = yaml.load(open('db.yaml'))

app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DATABASE'] = db['mysql_database']
app.config['MYSQL_HOST'] = db['mysql_host']

mysql = MySQL(app)

# cursor = mysql.connection.cursor()


from routes import *

# if __name__ == '__main__':
#     app.run(debug=True)

