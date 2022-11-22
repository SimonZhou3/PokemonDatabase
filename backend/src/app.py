from flask import Flask
from route import routes
import asyncio
import sys

from flask_cors import CORS

# Connect to an existing database

app = Flask(__name__)
CORS(app)

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

routes(app)
