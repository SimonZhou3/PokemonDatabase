from init_DB.initPokemonAreaVersion import init as initPokemonAreaVersionTable
from init_DB.initPokemonAreaVersion import insert as insertPokemonAreaVersionTable
#change this according to API resource names\
api_name = "null"
table = "pokemon_area"
table_id = "pokemon_area_id"
parent = "pokemon"
fk_id = parent+"_id"
parent2 = "area"
fk2_id = parent2+"_id"

populate_table = True

#index for child id
pokemon_area_version_id = 1

def init(cur, pb):
#if the table exist then skip entirely
    cur.execute("SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name='"+table+"')")
    if bool(cur.fetchone()[0]):
        print("**table " + table + " exists already**")
        populate_table = False
    else :

    # Execute a command: this creates a new table
        cur.execute("""
            CREATE TABLE """ + table + """ (
                """+ table_id + """  integer PRIMARY KEY,
                """+fk_id+""" integer,
                """+fk2_id+""" integer,
                """+fk3_id+""" integer,
                CONSTRAINT fk_"""+fk_id +"""
                    FOREIGN KEY("""+fk_id+""")
                        REFERENCES """+parent+"""("""+fk_id+""")
                        ON DELETE CASCADE,
                CONSTRAINT fk_"""+fk2_id+"""  
                    FOREIGN KEY("""+fk2_id+""")
                    REFERENCES """+parent2+"""("""+fk2_id+""")
                    ON DELETE CASCADE
                    )
            """)
        print("!!table " + table + " created!!")
    #create tables of dependent entities
    initPokemonAreaVersionTable(cur, pb)

def insert(cur, pb, area, versions, parent_id, id):
    #populate this table
    if populate_table:
        cur.execute(
            "SELECT area_id FROM area WHERE name = '" + area.name+"'"
        )
        area_id = cur.fetchone()[0]
        cur.execute(
            "INSERT INTO " +  table + " (" + table_id + ", " + fk_id + ", "+ fk2_id + ") VALUES (%s, %s, %s)",
            (id , parent_id, area_id))

    #populate child tables 
    global pokemon_area_version_id
    for version in versions:
        insertPokemonAreaVersionTable(cur, pb, version, id, pokemon_area_version_id)
        pokemon_area_version_id+=1