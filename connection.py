
import pymongo


client = pymongo.MongoClient("mongodb+srv://manjunathsirur:Jack_3140@test.y1bdo.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)


d = {
    'name':'manju',
    'email':'manjunathsirur1994@gmail.com',
    'sir_name':'sirur'
}

d1 = {
    'name':'manju',
    'email':'manjunathsirur1994@gmail.com',
    'sir_name':'sirur'
}

d2 = {
    'name':'manju',
    'email':'manjunathsirur1994@gmail.com',
    'sir_name':'sirur'
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)