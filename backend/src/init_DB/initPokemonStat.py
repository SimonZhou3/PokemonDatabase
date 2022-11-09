# change this according to API resource names\
api_name = "null"
table = "pokemon_stat"
table_id = table + "_id"
parent = "pokemon_generic"
fk_id = parent + "_id"
parent2 = "stat"
fk2_id = parent2 + "_id"

populate_table = True

# index for child id
child_id = 1

def init(cur, pb):
    global populate_table
    # if the table exist then skip entirely
    cur.execute("SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name='" + table + "')")
    if bool(cur.fetchone()[0]):
        print("**table " + table + " exists already**")
        populate_table = False
    else:

        # Execute a command: this creates a new table
        cur.execute("""
            CREATE TABLE """ + table + """ (
                """ + fk_id + """ integer PRIMARY KEY,
                hp integer,
                attack integer,
                defence integer,
                special_attack integer,
                special_defence integer,
                speed integer,
                CONSTRAINT fk_""" + fk_id + """
                    FOREIGN KEY(""" + fk_id + """)
                        REFERENCES """ + parent + """(""" + fk_id + """)
                        ON DELETE CASCADE
                    )
            """)
        print("!!table " + table + " created!!")
    # create tables of dependent entities
    # initChildTable(cur, pb)

def insert(cur, pb, stat, pokemon_id, id):
    # populate this table
    if populate_table:
        # Every pokemon will have a stat and the order will ALWAYS be the following: hp, attack, defence, special-attack, special_defence, speed
        pokemon_specific_stat = []
        for poke_stat in stat:
            pokemon_specific_stat.append(poke_stat.base_stat)

        print(pokemon_specific_stat)
        cur.execute(
            "INSERT INTO " + table + " (" + table_id + ", " + fk_id + ", hp,  attack, defence, special_attack, special_defence, speed ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (id, pokemon_id, pokemon_specific_stat[0], pokemon_specific_stat[1], pokemon_specific_stat[2],
             pokemon_specific_stat[3], pokemon_specific_stat[4], pokemon_specific_stat[5]))
