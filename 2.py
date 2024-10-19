import random
import time
import os


def generate_password():
    password = ""
    for i in range(6):
        password += str(random.randint(0, 9))
    print(password)


# generate_password()
# timer = 6
# while timer > 0:
#     time.sleep(1)
#     timer -= 1
#     if timer == 1:
#         generate_password()
#         timer = 6

while True:
    print("Your password is ", end="")
    generate_password()
    time.sleep(6)
    os.system("cls")
