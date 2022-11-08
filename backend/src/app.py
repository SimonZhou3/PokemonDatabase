from flask import Flask
import psycopg
import pokebase as pb
import os
from os.path import join, dirname
from dotenv import load_dotenv
from route import routes
from init_DB.initGeneration import init as initGeneration
import asyncio
import sys

#make sure postgres is running before running this
#i keep forgetting
#sudo systemctl start postgresql.service
#psql -d myDatabaseName

#Load environmental variables
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
DBNAME = os.environ.get('DBNAME')
USER = os.environ.get('USER')
PASSWORD = os.environ.get('PASSWORD')

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Connect to an existing database
# with psycopg.connect(F"dbname={DBNAME} user={USER} password={PASSWORD}") as conn:
#         # Open a cursor to perform database operations
#     with conn.cursor() as cur:
#         #wipe database
#         cur.execute("DROP SCHEMA public CASCADE")
#         cur.execute("CREATE SCHEMA public")
#         #initialize tables
#         initGeneration(cur, pb)
#         # Make the changes to the database persistent
#         conn.commit()
#         print("commited to database")
app = Flask(__name__)

routes(app)



