import json


def exctract_names(states):
    data = json.load(states)

    for i in data["states"]:
        if i["name"].lower() in ["new york", "alaska", "florida"]:
            print(i)


file = open("states.json")
exctract_names(file)
