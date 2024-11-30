import json

file = open("payments.json")
data = json.load(file)
salaries = {}

for i in data["employees"]:
    payment = sum(i["monthly_payment"].values())
    salaries.setdefault(i["name"], payment)

max_salary = max(salaries.values())

for k, v in salaries.items():
    if v == max_salary:
        print(k, ":", v)
