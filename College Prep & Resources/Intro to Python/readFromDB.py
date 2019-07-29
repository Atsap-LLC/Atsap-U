import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['stats'] #Connect to the stats database

mycol = mydb["homeruns"] #connect to the homeruns collection

stats = [{ "player": "John", "homeruns": 24},{ "player": "Collin", "homeruns": 9},{ "player": "Antonino", "homeruns": 33},{ "player": "Jim", "homeruns": 28},{ "player": "Gary", "homeruns": 7}]

for x in mycol.find(): # .find() method grabs all records in that collection.
    print(x)