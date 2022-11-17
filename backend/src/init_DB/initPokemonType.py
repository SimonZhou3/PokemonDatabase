# change this according to API resource names\
api_name = "null"
table = "pokemon_type"
table_id = table + "_id"
parent = "pokemon_generic"
fk_id = parent + "_id"
parent2 = "type"
fk2_id = parent2 + "_id"

populate_table = True

# index for child id
child_id = 1


def insert(cur, pb, poke_type, pokemon_id, id):
    # populate this table
    if populate_table:
        cur.execute(
            "SELECT type_id FROM type WHERE name = '" + poke_type.type.name + "'"
        )
        type_id = cur.fetchone()[0]
        print("TUPLE(POKEMON_TYPE): ", id, pokemon_id, type_id, poke_type.slot)
        cur.execute(
            "INSERT INTO " + table + " (" + table_id + ", " + fk_id + ", " + fk2_id + ", slot) VALUES (%s, %s, %s, %s)",
            (id, pokemon_id, type_id, poke_type.slot))
