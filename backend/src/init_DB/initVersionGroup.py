from init_DB.initVersion import insert as insertVersionTable

# change this according to API resource names\
api_name = "version-group"
table = "version_group"
table_id = table + "_id"
parent = "generation"
fk_id = parent + "_id"

populate_table = True

# index for child id
version_id = 1

def insert(cur, pb, version_group, generation_id, id):
    # resource = pb.APIresource(api_name,resource_name)
    if populate_table:
        print("TUPLE: ", id, version_group.name, generation_id)
        cur.execute(
            "INSERT INTO " + table + " (name, " + fk_id + ") VALUES (%s, %s)",
            (version_group.name, generation_id))

    global version_id
    for version in version_group.versions:
        insertVersionTable(cur, pb, version, id, version_id)
        version_id += 1
