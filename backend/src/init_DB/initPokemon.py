# TODO -- Add description to table by calling PokemonSpecies. REMEMBER THAT many pokemons can be in different versions.
#change this according to API resource names
api_name = "pokemon"
table = api_name
table_id = table+"_id"
# parent = ""
# fk_id = parent+"_id"

populate_table = True

#index for child id
child_id = 1

def init(cur, pb):
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
                name text)
            """)
        print("!!table " + table + " created!!")
        populate_table = True
    #create tables of dependent entities
    # initChildTable(cur, pb)

    #get list of pokemon
    resourceList = pb.APIResourceList(api_name)
    for id, item in enumerate(resourceList):
        #insert into pokemon table
        resource = pb.APIResource(api_name, item['name']);
        print(resource.name)
        if populate_table:
            cur.execute(
                "INSERT INTO " +  table + " (" + table_id + ", name) VALUES (%s, %s)",
                (id + 1 , resource.name,))



# charmander -> generation 1 -> gerneation 8
#