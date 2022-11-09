from flask import Flask
import psycopg
import pokebase as pb
# import os
# from os.path import join, dirname
# from dotenv import load_dotenv
from route import routes
from init_DB.initGeneration import init as initGeneration
from init_DB.initType import init as initType
from init_DB.initPokemonGeneric import init as initPokemon
from init_DB.initItem import init as initItem
from init_DB.initStat import init as initStat

# make sure postgres is running before running this
# i keep forgetting
# sudo systemctl start postgresql.service
# psql -d myDatabaseName

# Load environmental variables
# dotenv_path = join(dirname(__file__), '.env')
# load_dotenv(dotenv_path)
# DBNAME = os.environ.get('DBNAME')
# USER = os.environ.get('USER')
# PASSWORD = os.environ.get('PASSWORD')

# Connect to an existing database
with psycopg.connect(F"dbname=304 user=keqi") as conn:
    # Open a cursor to perform database operations
    with conn.cursor() as cur:
        # wipe database
        cur.execute("DROP SCHEMA public CASCADE")
        cur.execute("CREATE SCHEMA public")
        # initialize tables
        initGeneration(cur, pb)
        initType(cur, pb)
        initItem(cur,pb)
        initStat(cur,pb)
        initPokemon(cur, pb)
        # Make the changes to the database persistent
        conn.commit()
        print("commited to database")

app = Flask(__name__)

# routes(app)
