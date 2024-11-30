import json

file = open("states.json")
data = json.load(file)

for i in data["states"]:
    print(i["name"])
