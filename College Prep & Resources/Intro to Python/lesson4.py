import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['stats'] #Connect to the stats database

mycol = mydb["homeruns"] #connect to the homeruns collection

stats = [{ "player": "John", "homeruns": 24},{ "player": "Collin", "homeruns": 9},{ "player": "Antonino", "homeruns": 33},{ "player": "Jim", "homeruns": 28},{ "player": "Gary", "homeruns": 7}]

for x in mycol.find(): # .find() method grabs all records in that collection.
    print(x)
    new_HRS = x["homeruns"] #This gets the homerun value for each record.
    new_HRS = new_HRS + 5
    myquery = x # Search for current record
    newvalues = { "$set": { "homeruns": new_HRS } }
    mycol.update_one(myquery, newvalues)
