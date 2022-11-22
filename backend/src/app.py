from flask import Flask
from route import routes

from flask_cors import CORS

# Connect to an existing database

app = Flask(__name__)
CORS(app)

routes(app)
