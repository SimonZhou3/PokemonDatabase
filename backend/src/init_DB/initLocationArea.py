#change this according to API resource names\
api_name = "location-area"
table = "area"
table_id = table+"_id"
parent = "location"
fk_id = parent+"_id"

populate_table = True

#index for child id
child_id = 1

def insert(cur, pb, area, location_id, id):
    #populate this table
    if populate_table:
        print("TUPLE(AREA): ", id, area.name, location_id)
        cur.execute(
            "INSERT INTO " +  table + " (name, "+fk_id+") VALUES (%s, %s)",
            (area.name, location_id))