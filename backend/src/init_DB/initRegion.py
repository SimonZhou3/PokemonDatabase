from init_DB.initLocation import insert as insertLocationTable
#change this according to API resource names\
api_name = "region"
table = api_name
table_id = table+"_id"
parent = "generation"
fk_id = parent+"_id"

populate_table = True

#index for child id
location_id = 1

def insert(cur, pb, region, generation_id, id):
    # resource = pb.APIresource(api_name,resource_name)
    print("TUPLE(REGION): ", id, region.name, generation_id)
    if populate_table:
        cur.execute(
            "INSERT INTO " +  table + " (name, "+fk_id+") VALUES (%s, %s)",
            (region.name, generation_id))

    global location_id  
    for location in region.locations:
        insertLocationTable(cur, pb, location, id, location_id)
        location_id += 1

