import psycopg
import os
import pokebase as pb
from os.path import join, dirname
from dotenv import load_dotenv
from init_DB.initGeneration import init as initGeneration
from init_DB.initType import init as initType
import asyncio
import sys
from init_DB.initPokemonGeneric import init as initPokemon
from init_DB.initItem import init as initItem

# Load environmental variables
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
DBNAME = os.environ.get('DBNAME')
USER = os.environ.get('DBUSER')
PASSWORD = os.environ.get('PASSWORD')
PORT = os.environ.get('PORT')
HOST = os.environ.get('HOST')
SSLMODE = os.environ.get('SSLMODE')

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

conn = psycopg.connect(F"dbname={DBNAME} user={USER} password={PASSWORD} port={PORT} host={HOST} sslmode = {SSLMODE}")
print('Connected to DB')
# Open a cursor to perform database operations
with conn.cursor() as cur:
    # initialize tables
    initGeneration(cur, pb)
    initItem(cur, pb)
    initType(cur,pb)
    initPokemon(cur, pb)
    conn.commit()
    print("commited to database")