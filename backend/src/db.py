import psycopg
import os
from os.path import join, dirname
from dotenv import load_dotenv

# Load env variables
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
DBNAME = os.environ.get('DBNAME')
USER = os.environ.get('USER')
PASSWORD = os.environ.get('PASSWORD')

class Database:

    @staticmethod
    async def execute(SQL,params):
        async with await psycopg.AsyncConnection.connect(F"dbname={DBNAME} user={USER} password={PASSWORD}") as aconn:
            async with aconn.cursor() as cur:
                await cur.execute(SQL,params)
                return await cur.fetchall()

                