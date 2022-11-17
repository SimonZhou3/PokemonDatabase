from init_DB.initVersionGroup import insert as insertVersionTable
from init_DB.initRegion import insert as insertRegionTable
#change this according to API resource names
api_name = "generation"
table = api_name
table_id = table + "_id"

populate_table = True

#index for child id
version_id = 1
region_id = 1

def init(cur, pb):
    global populate_table
    global version_id
    global region_id

    #get list of all generations
    generationList = pb.APIResourceList(api_name)
    for id, item in enumerate(generationList):
    # Pass data to fill a query placeholders and let Psycopg perform
    # the correct conversion (no SQL injections!)

        #insert into generation table
        generation = pb.APIResource(api_name, item['name'])
        if populate_table:
            generation.name = generation.name.replace("-", " ")
            print("TUPLE(GENERATION): ", id + 1, generation.name)
            cur.execute(
                "INSERT INTO " +  table + " (name) VALUES (%s)",
                (generation.name,))
        
        #insert into version_group table
        for version in generation.version_groups:
            insertVersionTable(cur, pb, version, id + 1, version_id)
            version_id += 1
        
        #insert into region table
        insertRegionTable(cur, pb, generation.main_region, id + 1, region_id)
        region_id += 1
