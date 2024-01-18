import psycopg2
from sqlite_example import connect_to_db, execute_q
from queries import CREATE_CHARACTERS_TABLE
from queries import SELECT_CHARACTER, DROP_CHARACTERS_TABLE

# PG connection credentials

# "User & Default database" from ElephantSQL
DBNAME = 'ldfljsbn'
USER = 'ldfljsbn'
# "Password" from ElephantSQL
PASSWORD = ''
# "Server" from ElephantSQL
HOST = 'heffalump.db.elephantsql.com'

def connect_to_pg(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST):
    pg_conn = psycopg2.connect(dbname=DBNAME, user=USER,
                           password=PASSWORD, host=HOST)
    pg_curs = pg_conn.cursor()
    return pg_conn, pg_curs

def modify_db(conn, curs, queries):
    for q in queries:
        curs.execute(q)
    conn.commit()

def pipe_rgb_sqlite_to_pg():
    '''
    (1) function uses the connect_to_db function from sqlite_example.py to connect to
    sqlite3.
    (2) calls execute_q function from sqlite_example.py with the SELECT_CHARACTER
    query from queries.py to access the "charactercreator_character" table.
    (3) iterates over every line in "charactercreator_character", placing each
    line's attributes in the query: q_insert.
    (4) creates an empty list and appends each instance of q_insert.
    (5) calls connect_to_pg to connect to postgress.
    (6) calls modify_pg to reset and then create the empty table: "characters"
    in postgress.
    (7) calls modify_pg with insert_list, the list containing the query to insert
    every line of "charactercreator_character" into "characters"
    '''
    conn = connect_to_db()
    result = execute_q(conn, SELECT_CHARACTER)

    insert_list = []

    for tup in result:
        q_insert = f'''
        INSERT INTO characters ("character_id", "name", "level", "exp", "hp",
                            "strength", "intelligence",
                            "dexterity", "wisdom")
        VALUES {tup};
        '''
        insert_list.append(q_insert)

    queries = (DROP_CHARACTERS_TABLE, CREATE_CHARACTERS_TABLE)

    pg_conn, pg_curs = connect_to_pg()
    modify_db(pg_conn, pg_curs, queries)
    modify_db(pg_conn, pg_curs, insert_list)


if __name__ =="__main__":
    conn = connect_to_db()
    print(execute_q(conn, SELECT_CHARACTER)[:2])
    
