#change this according to API resource names\
api_name = "null"
table = "pokemon_type"
table_id = table+"_id"
parent = "pokemon_generic"
fk_id = parent+"_id"
parent2 = "type"
fk2_id = parent2+"_id"

populate_table = True

#index for child id
child_id = 1

def init(cur, pb):
    global populate_table
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
                slot integer,
                """+fk_id+""" integer,
                """+fk2_id+""" integer,
                CONSTRAINT fk_"""+fk_id +"""
                    FOREIGN KEY("""+fk_id+""")
                        REFERENCES """+parent+"""("""+fk_id+""")
                        ON DELETE CASCADE,
                CONSTRAINT fk_"""+fk2_id +"""
                    FOREIGN KEY("""+fk2_id+""")
                        REFERENCES """+parent2+"""("""+fk2_id+""")
                        ON DELETE CASCADE
                    )
            """)
        print("!!table " + table + " created!!")
    #create tables of dependent entities
    # initChildTable(cur, pb)

def insert(cur, pb, poke_type, pokemon_id, id):
    #populate this table
    if populate_table:
        cur.execute(
            "SELECT type_id FROM type WHERE name = '" + poke_type.type.name+"'"
        )
        type_id = cur.fetchone()[0]
        print("TUPLE(POKEMON_TYPE): ", id, pokemon_id, type_id, poke_type.slot)
        cur.execute(
            "INSERT INTO " +  table + " (" + table_id + ", " + fk_id + ", " + fk2_id + ", slot) VALUES (%s, %s, %s, %s)",
            (id , pokemon_id, type_id, poke_type.slot))

    # #populate child tables
    # global child_id
    # for child in resource.children:
    #     insertChildTable(cur, pb, area, id, child_id)
    #     child_id += 1
