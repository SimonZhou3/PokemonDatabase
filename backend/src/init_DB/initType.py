from init_DB.initMove import insert as insertMoveTable
#change this according to API resource names\
api_name = "type"
table = api_name
table_id = table+"_id"
# parent = ""
# fk_id = parent+"_id"

populate_table = True

#index for child id
moveIndex = 1

def init(cur, pb):
    global populate_table

    typeList = pb.APIResourceList(api_name)
    typeIndex = 1
    for typeID in typeList:
        poke_type = pb.APIResource(api_name, typeID['name'])
        #populate this table
        if populate_table:
            print("TUPLE(TYPE): ", typeIndex, poke_type.name)
            cur.execute(
                "INSERT INTO " +  table + " (" + table_id + ", name"+") VALUES (%s, %s)",
                (typeIndex , poke_type.name))

        global moveIndex
        for move in poke_type.moves:
            insertMoveTable(cur, pb, move, typeIndex, moveIndex)
            moveIndex += 1
        typeIndex+=1


