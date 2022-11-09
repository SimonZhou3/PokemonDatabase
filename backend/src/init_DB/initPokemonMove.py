#change this according to API resource names\
api_name = "null"
table = "pokemon_move"
table_id = table+"_id"
parent = "pokemon_specific"
fk_id = parent+"_id"
parent2= "move"
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
                """+fk_id+""" integer,
                """+fk2_id+""" integer,
                method text,
                level integer,
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

def insert(cur, pb, move, poke_move_version, pokemon_id, id):
    #populate this table
    if populate_table:
        #get move_id
        cur.execute(
            "SELECT move_id FROM move WHERE name = '" + move.name+"'"
        )
        move_id = cur.fetchone()[0]
        #get_specific_pokemon_id
        cur.execute(
            "SELECT version_group_id FROM version_group WHERE name = '" + poke_move_version.version_group.name+"'"
        )
        version_group_id = cur.fetchone()[0]
        cur.execute(
            "SELECT version_id FROM version WHERE version_group_id = '" + str(version_group_id)+"'"
        )
        version_ids = cur.fetchall()
        # print(version_ids)
        pokemon_specific_ids = []
        for version_id in version_ids:
            cur.execute(
                "SELECT pokemon_specific_id FROM pokemon_specific WHERE pokemon_generic_id = '" + str(pokemon_id) + "'"
                " AND version_id = '" + str(version_id[0]) +"'"
            )
            poke_id = cur.fetchone()
            if poke_id is not None:
                pokemon_specific_ids.append(poke_id[0])
        # print(pokemon_specific_ids)
        for pokemon_specific_id in pokemon_specific_ids:
            print("TUPLE(POKEMON_MOVE): ", id, pokemon_specific_id, move_id, poke_move_version.move_learn_method.name, poke_move_version.level_learned_at)
            cur.execute(
                "INSERT INTO " +  table + " (" + table_id + ", "+ fk_id + ", " + fk2_id + ", method, level) VALUES (%s, %s, %s, %s, %s)",
                (id, pokemon_specific_id, move_id, poke_move_version.move_learn_method.name, poke_move_version.level_learned_at))
            id +=1
        return id
    # #populate child tables 
    # global child_id
    # for child in resource.children:
    #     insertChildTable(cur, pb, area, id, child_id)
    #     child_id += 1