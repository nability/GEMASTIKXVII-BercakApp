from flask import Flask, session, flash, redirect, url_for, render_template
from flask_restful import Api
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
# from utils_flask import capture_image

app = Flask(__name__)
api = Api(app)
bcrypt = Bcrypt(app)
db = MySQL(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db_gemastik'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

app.config["SECRET_KEY"] = 'RahasiaKabupatenSukabumi'
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

from routes import *

if __name__== "__main__":
   # capture_image()
   app.run(debug=True)
