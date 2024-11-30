import json

file = open("payments.json")
data = json.load(file)

for i in data["employees"]:
    print(i["name"], ":", i["job_title"])
