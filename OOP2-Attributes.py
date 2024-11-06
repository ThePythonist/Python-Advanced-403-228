class SedanCar:
    # Class Attribute
    zarfiat = 5
    darha = 4

    # Instance Attribute
    def __init__(self, horsepower):
        self.hp = horsepower


# Accessing class attribute
# print(SedanCar.zarfiat)
# print(SedanCar.darha)

# Creating instances
persia = SedanCar(105)
dena = SedanCar(115)

# Accessing instance attribute
# print(persia.hp)
# print(dena.hp)

# Accessing class attribute
# print(persia.zarfiat)
# print(dena.zarfiat)

# Modifying instance attribute
# persia.hp = 140
# print(persia.hp)
# print(dena.hp)

# Modifying class attribute
SedanCar.zarfiat = 4
print(persia.zarfiat)
print(dena.zarfiat)
