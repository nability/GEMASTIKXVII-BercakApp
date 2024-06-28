from flask import Flask
from flask_restful import Api
import os

app = Flask(_name_)
api = Api(app)

from routes import *

if _name_ == "_main_":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))