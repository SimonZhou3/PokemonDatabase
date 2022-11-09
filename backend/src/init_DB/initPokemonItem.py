# change this according to API resource names\
api_name = "null"
table = "pokemon_item"
table_id = table + "_id"
parent = "pokemon_specific"
fk_id = parent + "_id"
parent2 = "item"
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
                """ + table_id + """  integer PRIMARY KEY,
                """ + fk_id + """ integer,
                """ + fk2_id + """ integer,
                rarity integer,
                CONSTRAINT fk_""" + fk_id + """
                    FOREIGN KEY(""" + fk_id + """)
                        REFERENCES """ + parent + """(""" + fk_id + """)
                        ON DELETE CASCADE,
                CONSTRAINT fk_""" + fk2_id + """
                    FOREIGN KEY(""" + fk2_id + """)
                        REFERENCES """ + parent2 + """(""" + fk2_id + """)
                        ON DELETE CASCADE
                    )
            """)
        print("!!table " + table + " created!!")
    # create tables of dependent entities
    # initChildTable(cur, pb)


def insert(cur, pb, item, poke_held_item_version, pokemon_id, id):
    # populate this table
    if populate_table:
        # get item_id
        cur.execute(
            "SELECT item_id FROM item WHERE name = '" + item.name + "'"
        )
        item_id = cur.fetchone()[0]
        # get_specific_pokemon_id
        cur.execute(
            "SELECT version_id FROM version WHERE name = '" + poke_held_item_version.version.name + "'"
        )
        version_id = cur.fetchone()[0]
        # print(version_ids)
        pokemon_specific_ids = []
        cur.execute(
            "SELECT pokemon_specific_id FROM pokemon_specific WHERE pokemon_generic_id = '" + str(pokemon_id) + "' AND version_id = '" + str(version_id) + "'"
        )
        poke_id = cur.fetchone()
        if poke_id is not None:
            pokemon_specific_ids.append(poke_id[0])
        # print(pokemon_specific_ids)
        for pokemon_specific_id in pokemon_specific_ids:
            print("TUPLE(POKEMON_ITEM): ", id, pokemon_specific_id, item_id, poke_held_item_version.rarity)
            cur.execute(
                "INSERT INTO " + table + " (" + table_id + ", " + fk_id + ", " + fk2_id + ", rarity) VALUES (%s, %s, %s, %s)",
                (id, pokemon_specific_id, item_id, poke_held_item_version.rarity))
            id += 1
        return id
    # #populate child tables
    # global child_id
    # for child in resource.children:
    #     insertChildTable(cur, pb, area, id, child_id)
    #     child_id += 1
