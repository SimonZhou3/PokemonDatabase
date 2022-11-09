#change this according to API resource names\
api_name = "pokemon"
table = "pokemon_specific"
table_id = table+"_id"
parent = "pokemon_generic"
fk_id = parent+"_id"
parent2 = "version"
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
                """+ table_id + """  integer UNIQUE,
                """+fk_id+""" integer,
                """+fk2_id+""" integer,
                description text,
                PRIMARY KEY ("""+fk_id+""", """+fk2_id+"""),
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

def insert(cur, pb, version, descs, pokemon_id, id):
    #populate this table
    if populate_table:
        #get version_id
        cur.execute(
            "SELECT version_id FROM version WHERE name = '" + version.name+"'"
        )
        version_id = cur.fetchone()[0]
        #get version_group_name
        # cur.execute(
        #     """SELECT DISTINCT version_group.name
        #     FROM version_group
        #     INNER JOIN version
        #     ON version.version_group_id = version_group.version_group_id AND version_id = '"""
        #     + str(version_id) + """'"""
        # )
        # version_group_name = cur.fetchone()[0]
        # print(version_group_name)
        description = "No Description"
        for desc in descs:
            if desc.version.name == version.name:
                if desc.language.name == "en":
                    description = desc.flavor_text
                    break
        print("TUPLE(POKEMON_SPECIFIC): ", id, pokemon_id, version_id, description)
        cur.execute(
            "INSERT INTO " +  table + " (" + table_id + ", " + fk_id + ", " + fk2_id + ", description) VALUES (%s, %s, %s, %s)",
            (id , pokemon_id, version_id, description))

    # #populate child tables
    # global child_id
    # for child in resource.children:
    #     insertChildTable(cur, pb, area, id, child_id)
    #     child_id += 1
