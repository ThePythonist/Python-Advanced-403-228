import json


def exctract_names(states):
    data = json.load(states)
    names = []

    for i in data["states"]:
        names.append(i["name"])

    new_file = open("state_names.json", "w")
    json.dump(names, new_file, indent=2)

    print("extracted and saved in state_names.json")


file = open("states.json")
exctract_names(file)
