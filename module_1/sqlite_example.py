import sqlite3
import queries as q
import pandas as pd

'''
# step 1 - connection
connection = sqlite3.connect('rpg_db.sqlite3')

# step 2 - cursor
cursor = connection.cursor()

# step 3 - write query
query = 'SELECT character_id, name FROM charactercreator_character;'

# step 4 - execute the query on the cursor and fatch the results
# "pulling the results from the cursor"
results = cursor.execute(query).fetchall()
'''

# consolodate steps into reusable functions

def connect_to_db(db='rpg_db.sqlite3'):
    return sqlite3.connect(db)

def execute_q(conn, query):
    curs = conn.cursor()
    curs.execute(query)
    return curs.fetchall()

if __name__ == '__main__':
    conn = connect_to_db()
    results = execute_q(conn, q.AVG_ITEM_WEIGHT_PER_CHAR)[:5]
    df = pd.DataFrame(results)
    print(df.head)