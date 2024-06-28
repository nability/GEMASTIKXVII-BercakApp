from flask import Flask
from flask_restful import Api

app = Flask(_name_)
api = Api(app)

from routes import *

if _name== "main_":
   app.run(debug=True)