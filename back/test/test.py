import json 

with open("example.json", "r") as json_file:
    a = json.load(json_file)

# print(a["Name"])
# print(a.keys())

# del a["Media"]["OnlyFans"]
# print(a)

# только python словарь 
# a["Mass"] = [1, "h", {"a": 1}, [1, 2, 3]]
# print(a)

a["Mass"] = [1, "h", {"a": 1}, [1, 2, 3]]
print(json.dumps(a, indent = 2 ))

with open("example.json", "w") as json_file:
    json.dump(a, json_file, indent = 2)
