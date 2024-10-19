from faker import Faker
fake = Faker()

print(fake.name())
print(fake.country())
print(fake.city())
print(fake.email())
print(fake.postalcode())
print(fake.random_letters(3))