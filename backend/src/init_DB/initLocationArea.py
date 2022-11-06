#change this according to API resource names\
api_name = "location-area"
table = "area"
table_id = table + "_id"

def init(cur, pb):
#if the table exist then skip entirely
#if need to remake the table, enter DROP TABLE tablename; before running
    cur.execute("SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name='"+table+"')")
    if bool(cur.fetchone()[0]):
        print("**table " + table + " exists already**")
    else :

    # Execute a command: this creates a new table
        cur.execute("""
            CREATE TABLE """ + table + """ (
                """+ table_id + """  integer PRIMARY KEY,
                name text,
                location_id integer,
                CONSTRAINT fk_location_id
                    FOREIGN KEY(location_id)
                        REFERENCES location(location_id)
                        ON DELETE CASCADE
                    )
            """)
        print("!!table " + table + " created!!")


def insert(cur,pb,resource,parent_id, child_id):
    cur.execute(
        "INSERT INTO " +  table + " (" + table_id + ", name, location_id) VALUES (%s, %s, %s)",
        (child_id , resource.name, parent_id))