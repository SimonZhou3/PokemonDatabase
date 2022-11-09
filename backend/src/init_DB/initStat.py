#change this according to API resource names
api_name = "stat"
table = api_name
table_id = table + "_id"

populate_table = True

#index for child id

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
                    name text UNIQUE,
                    battle_only boolean)
                    """)
        print("!!table " + table + " created!!")
        populate_table = True
    #create tables of dependent entities


    #get list of all generations
    statList = pb.APIResourceList(api_name)
    stat_index = 1
    for stat_id in statList:
        # Pass data to fill a query placeholders and let Psycopg perform
        # the correct conversion (no SQL injections!)

        #insert into generation table
        stat = pb.APIResource(api_name, stat_id['name'])
        print("TUPLE(STAT): ", stat_index, stat.name, stat.is_battle_only)
        if populate_table:
            cur.execute(
                "INSERT INTO " +  table + " (" + table_id + ", name, battle_only) VALUES (%s, %s, %s)",
                (stat_index, stat.name, stat.is_battle_only))

        stat_index += 1


    # Query the database and obtain data as Python objects.
    # cur.execute("SELECT * FROM " + table)
    # cur.fetchone()
    # will return (1, 1996-02-27, "red")

    # You can use `cur.fetchmany()`, `cur.fetchall()` to return a list
    # of several records, or even iterate on the cursor
    # for record in cur:
    #     print(record)