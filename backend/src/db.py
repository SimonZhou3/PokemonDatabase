import psycopg
from psycopg_pool import AsyncConnectionPool
import os
from os.path import join, dirname
from dotenv import load_dotenv

# Load env variables
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
DBNAME = os.environ.get('DBNAME')
USER = os.environ.get('DBUSER')
PASSWORD = os.environ.get('PASSWORD')
PORT = os.environ.get('PORT')
HOST = os.environ.get('HOST')
SSLMODE = os.environ.get('SSLMODE')

POOL = None

class Database:
    @staticmethod 
    async def getPool():
        global POOL
        if (POOL is None):
            POOL = AsyncConnectionPool(F"dbname={DBNAME} user={USER} password={PASSWORD} port={PORT} host={HOST} sslmode = {SSLMODE}")
            return POOL

        else:
            return POOL


    @staticmethod
    async def execute(SQL,params):
                pool = await Database.getPool()
                async with pool.connection() as aconn:
                    async with aconn.cursor() as cur:
                        await cur.execute(SQL,params)
                        aconn.commit()
                        return await cur.fetchall()

                