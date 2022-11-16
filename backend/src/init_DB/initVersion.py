# change this according to API resource names\
api_name = "version"
table = api_name
table_id = table + "_id"
parent = "version_group"
fk_id = parent + "_id"

populate_table = True

version_release = {
    'red': '1996-02-27', 'blue': '1996-10-15', 'yellow': '1998-10-12',
    'gold': '1999-11-21', 'silver': '1999-11-21', 'crystal': '2000-12-14',
    'ruby': '2002-11-21', 'sapphire': '2002-11-21', 'emerald': '2004-09-16',
    'firered': '2004-01-29', 'leafgreen': '2004-01-29', 'colosseum': '2003-11-21',
    'xd': '2005-08-04', 'diamond': '2006-09-28', 'pearl': '2006-09-28',
    'platinum': '2008-09-13', 'heartgold': '2009-09-12', 'soulsilver': '2009-09-12',
    'black': '2010-09-18', 'white': '2010-09-18', 'black-2': '2012-06-23', 'white-2': '2012-06-23',
    'x': '2013-10-12', 'y': '2013-10-12', 'omega-ruby': '2014-11-21',
    'alpha-sapphire': '2014-11-21', 'sun': '2016-11-18', 'moon': '2016-11-18', 'ultra-sun': '2017-11-17',
    'ultra-moon': '2017-11-17', 'lets-go-pikachu': '2018-11-16', 'lets-go-eevee': '2018-11-16',
    'sword': '2019-11-15', 'shield': '2019-11-15', 'the-isle-of-armor': '2020-06-17',
    'the-crown-tundra': '2020-10-22', 'brilliant-diamond': '2021-11-19', 'shining-pearl': '2021-11-19',
    'legends-arceus': '2022-01-28'
}

# index for child id
child_id = 1


def init(cur, pb):
    global populate_table
    # if the table exist then skip entirely
    cur.execute("SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name='" + table + "')")
    if bool(cur.fetchone()[0]):
        print("**table " + table + " exists already**")
        populate_table = False
    else:

        # Execute a command: this creates a new table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS """ + table + """ (
                """ + table_id + """ SERIAL PRIMARY KEY,
                name text,
                release_date date,
                """ + fk_id + """ integer,
                CONSTRAINT fk_""" + fk_id + """
                    FOREIGN KEY(""" + fk_id + """)
                        REFERENCES """ + parent + """(""" + fk_id + """)
                        ON DELETE CASCADE
                    )
            """)
        print("!!table " + table + " created!!")
    # create tables of dependent entities
    # initChildTable(cur, pb)


def insert(cur, pb, version, version_group_id, id):
    # populate this table
    if populate_table:
        print("TUPLE(VERSION): ", id, version.name, version_release[version.name], version_group_id)
        cur.execute(
            "INSERT INTO " + table + " (name, release_date, " + fk_id + ") VALUES (%s, %s, %s)",
            (version.name.replace("-", " "), version_release[version.name], version_group_id))
