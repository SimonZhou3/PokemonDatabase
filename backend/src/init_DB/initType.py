from init_DB.initMove import init as initMoveTable
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
    #if the table exist then skip entirely
    cur.execute("SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name='"+table+"')")
    if bool(cur.fetchone()[0]):
        print("**table " + table + " exists already**")
        populate_table = False
    else :

    # Execute a command: this creates a new table
        cur.execute("""
            CREATE TABLE """ + table + """ (
                """+ table_id + """  integer PRIMARY KEY,
                name text,
                damage_class text
                    )
            """)
        print("!!table " + table + " created!!")
        populate_table = True
    #create tables of dependent entities
    initMoveTable(cur, pb)

    typeList = pb.APIResourceList(api_name)
    typeIndex = 1
    for typeID in typeList:
        poke_type = pb.APIResource(api_name, typeID['name'])
        #populate this table
        if populate_table:
            cur.execute(
                "INSERT INTO " +  table + " (" + table_id + ", name"+") VALUES (%s, %s)",
                (typeIndex , poke_type.name))

        global moveIndex
        for move in poke_type.moves:
            insertMoveTable(cur, pb, move, typeIndex, moveIndex)
            moveIndex += 1
        typeIndex+=1

        #populate child tables
        # global child_id
        # for child in resource.children:
        #     insertChildTable(cur, pb, area, id, child_id)
        #     child_id += 1

