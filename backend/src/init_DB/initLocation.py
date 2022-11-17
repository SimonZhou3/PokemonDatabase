from init_DB.initLocationArea import insert as insertAreaTable
#change this according to API resource names\
api_name = "location"
table = api_name
table_id = table+"_id"
parent = "region"
fk_id = parent+"_id"

populate_table = True

#index for child id
area_id = 1

def insert(cur, pb, location, region_id, id):
    if populate_table:
        print("TUPLE(LOCATION): ", id, location.name, region_id)
        cur.execute(
            f"INSERT INTO {table} (name, {fk_id}) VALUES (%s, %s)",
            (location.name, region_id))
    
    global area_id
    for area in location.areas:
        insertAreaTable(cur, pb, area, id, area_id)
        area_id += 1
