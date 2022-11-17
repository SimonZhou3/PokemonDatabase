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

def insert(cur, pb, version, descs, pokemon_id, id):
    #populate this table
    if populate_table:
        #get version_id
        versionString = version.name.replace("-", " ")
        print("(DEBUGGING) -- " + versionString)
        cur.execute(
            "SELECT version_id FROM version WHERE name = '" + versionString +"'"
        )
        version_id = cur.fetchone()[0]

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

