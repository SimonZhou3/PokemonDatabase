from init_DB.initLocation import init as initLocationTable
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
                """+ table_id + """ SERIAL PRIMARY KEY,
                name text,
                """+fk_id+""" integer,
                CONSTRAINT fk_"""+fk_id +"""
                    FOREIGN KEY("""+fk_id+""")
                        REFERENCES """+parent+"""("""+fk_id+""")
                        ON DELETE CASCADE
                    )
            """)
        print("!!table " + table + " created!!")
    #create tables of dependent entities
    initLocationTable(cur,pb)

def insert(cur, pb, region, generation_id, id):
    # resource = pb.APIresource(api_name,resource_name)
    print("TUPLE(REGION): ", id, region.name, generation_id)
    if populate_table:
        cur.execute(
            "INSERT INTO " +  table + " (name, "+fk_id+") VALUES (%s, %s)",
            (resource.name, parent_id))

    global location_id  
    for location in region.locations:
        insertLocationTable(cur, pb, location, id, location_id)
        location_id += 1


    # Query the database and obtain data as Python objects.
    # cur.execute("SELECT * FROM " + table)
    # cur.fetchone()
    # will return (1, 1996-02-27, "red")

    # You can use `cur.fetchmany()`, `cur.fetchall()` to return a list
    # of several records, or even iterate on the cursor
    # for record in cur:
    #print(record)