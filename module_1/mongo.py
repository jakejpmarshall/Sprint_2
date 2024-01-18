import pymongo

char = [
    (1, 'Aliquid iste optio reiciendi', 0, 0, 10, 1, 1, 1, 1), 
    (2, 'Optio dolorem ex a', 0, 0, 10, 1, 1, 1, 1)
]

mongo_char = {
    'character_id':1,
    'name':'Aliquid iste optio reiciendi',
    'level':0,
    'exp':0,
    'hp':10,
    'strength':1,
    'intelligence':1,
    'dexterirty':1,
    'wisdom':1
}

DBNAME = 'test'
PASSWORD = ''

client = pymongo.MongoClient(f'mongodb+srv://jakejpmarshall:{PASSWORD}@cluster0.tzbq8uk.mongodb.net/?retryWrites=true&w=majority')
db = client[DBNAME]


if __name__ == '__main__':
    db.bit_o_mess.insert_one(mongo_char)
