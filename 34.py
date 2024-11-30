import json

file = open("payments.json")
data = json.load(file)

salaries = []

for i in data["employees"]:
    # avg = sum(i["monthly_payment"].values()) / 12
    # salaries.append(avg) # per month

    payment = sum(i["monthly_payment"].values())
    salaries.append(payment)  # per year

print("Average payment of employees :", sum(salaries) / len(salaries))
