import json

file = open("payments.json")
data = json.load(file)
employees = {}

for i in data["employees"]:
    emp_salary = [i for i in i["monthly_payment"].values()]
    avg = sum(emp_salary) / len(emp_salary)
    employees.setdefault(i["name"], avg)

# result = sorted(employees.items(), key=lambda t: t[1])
result = sorted(employees.items(), key=lambda t: t[1], reverse=True)
print(result)
