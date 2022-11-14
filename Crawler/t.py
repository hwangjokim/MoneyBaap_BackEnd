from pymongo import MongoClient
# from crawling import *
import json

f=open("db_token.txt","r")
tk=f.readline().rstrip()

client = MongoClient(tk)
f.close()
db = client.jdb
collection = db.foods

# save_unique_number(["숭실대맛집"])

# result = get_result("숭실대맛집")

# print(result)
# count=1
# for place in result:
#     collection.insert_one(place)
f=open("datas.json","w")
data = collection.find({})
for a in data:
    a.pop("_id")
    #print(a)
    f.write(json.dumps(a,ensure_ascii=False))
    f.write(",\n")
f.close()