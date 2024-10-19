from faker import Faker

fake = Faker()

people = []

for i in range(4):
    people.append({
        "name": fake.name(),
        "email": fake.email(),
        "country": fake.country(),
        "postalcode": fake.postalcode()
    })

for i in people:
    print(i)
