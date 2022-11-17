import psycopg
import os
from os.path import join, dirname
from dotenv import load_dotenv

# Load env variables
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
DBNAME = os.environ.get('DBNAMES')
USER = os.environ.get('DBUSER')
PASSWORD = os.environ.get('PASSWORD')
PORT = os.environ.get('PORT')
HOST = os.environ.get('HOST')
SSLMODE = os.environ.get('SSLMODE')

class Database:

    @staticmethod
    async def execute(SQL,params):
        async with await psycopg.AsyncConnection.connect(F"dbname={DBNAME} user={USER} password={PASSWORD} port={PORT} host={HOST} sslmode = {SSLMODE}") as aconn:
            async with aconn.cursor() as cur:
                await cur.execute(SQL,params)
                return await cur.fetchall()

                