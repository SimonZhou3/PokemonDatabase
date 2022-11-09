#change this according to API resource names\
api_name = "location-area"
table = "area"
table_id = table+"_id"
parent = "location"
fk_id = parent+"_id"

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
                name text,
                """+fk_id+""" integer,
                CONSTRAINT fk_"""+fk_id +"""
                    FOREIGN KEY("""+fk_id+""")
                        REFERENCES """+parent+"""("""+fk_id+""")
                        ON DELETE CASCADE
                    )
            """)
        print("!!table " + table + " created!!")
    #create tables of dependent entities
    # initChildTable(cur, pb)

def insert(cur, pb, area, location_id, id):
    #populate this table
    if populate_table:
        print("TUPLE(AREA): ", id, area.name, location_id)
        cur.execute(
            "INSERT INTO " +  table + " (" + table_id + ", name, "+fk_id+") VALUES (%s, %s, %s)",
            (id , area.name, location_id))
    
    #populate child tables 
    # global child_id
    # for child in resource.children:
    #     insertChildTable(cur, pb, area, id, child_id)
    #     child_id += 1
