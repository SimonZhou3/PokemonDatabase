#change this according to API resource names\
api_name = "move"
table = api_name
table_id = table+"_id"
parent = "type"
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
                """+fk_id+""" integer,
                name text,
                accuracy integer,
                effect_chance integer,
                pp integer,
                priority integer,
                power integer,
                damage_class text,
                CONSTRAINT fk_"""+fk_id +"""
                    FOREIGN KEY("""+fk_id+""")
                        REFERENCES """+parent+"""("""+fk_id+""")
                        ON DELETE CASCADE
                    )
            """)
        print("!!table " + table + " created!!")
    #create tables of dependent entities
    # initChildTable(cur, pb)

def insert(cur, pb, move, type_id, id):
    if populate_table:
        print("TUPLE(MOVE) :", id, move.name, type_id, move.accuracy, move.effect_chance, move.pp, move.priority, move.power, move.damage_class.name)
        cur.execute(
            "INSERT INTO " +  table + " (" + table_id + ", " + fk_id + ", name, accuracy, effect_chance, pp, priority, power, damage_class) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (id, type_id, move.name, move.accuracy, move.effect_chance, move.pp, move.priority, move.power, move.damage_class.name))

        #populate child tables
        # global child_id
        # for child in resource.children:
        #     insertChildTable(cur, pb, area, id, child_id)
        #     child_id += 1

