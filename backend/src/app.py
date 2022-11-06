from flask import Flask
import psycopg
import pokebase as pb
from init_DB.initGeneration import init as initGeneration
#make sure postgres is running before running this
#i keep forgetting
#sudo systemctl start postgresql.service
#psql -d myDatabaseName

# Connect to an existing database
with psycopg.connect("dbname=304 user=keqi") as conn:
        # Open a cursor to perform database operations
    with conn.cursor() as cur:
        #wipe database
        cur.execute("DROP SCHEMA public CASCADE")
        cur.execute("CREATE SCHEMA public")
        #initialize tables
        initGeneration(cur, pb)
        # Make the changes to the database persistent
        conn.commit()
        print("commited to database")

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>" 


