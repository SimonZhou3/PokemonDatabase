# change this according to API resource names\
api_name = "null"
table = "pokemon_area"
table_id = table + "_id"
parent = "pokemon_specific"
fk_id = parent + "_id"
parent2 = "area"
fk2_id = parent2 + "_id"

populate_table = True

# index for child id
child_id = 1

def insert(cur, pb, area, encounter_version, pokemon_id, id):
    # populate this table
    if populate_table:
        # get move_id
        cur.execute(
            "SELECT area_id FROM area WHERE name = '" + area.name + "'"
        )
        area_id = cur.fetchone()[0]
        # get_specific_pokemon_id
        versionString = encounter_version.version.name.replace("-", " ")
        print("(DEBUGGING) -- " + versionString)
        cur.execute(
        "SELECT version_id FROM version WHERE name = '" + versionString + "'"
        )
        version_id = cur.fetchone()[0]
        # print(version_id)
        pokemon_specific_ids = []
        cur.execute(
            "SELECT pokemon_specific_id FROM pokemon_specific WHERE pokemon_generic_id = '" + str(pokemon_id) + "'"
                                                                                                                " AND version_id = '" + str(
                version_id) + "'"
        )
        poke_id = cur.fetchone()
        if poke_id is not None:
            pokemon_specific_ids.append(poke_id[0])
        # print(pokemon_specific_ids)
        for pokemon_specific_id in pokemon_specific_ids:
            print("TUPLE(POKEMON_AREA): ", id, pokemon_specific_id, area_id, encounter_version.max_chance)
            cur.execute(
                "INSERT INTO " + table + " (" + fk_id + ", " + fk2_id + ", max_chance) VALUES (%s, %s, %s)",
                (pokemon_specific_id, area_id, encounter_version.max_chance))
            id += 1
        return id