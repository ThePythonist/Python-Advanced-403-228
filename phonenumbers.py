import random


def irancell():
    prefix = ["0939", "0930", "0936", "0933"]

    # n = random.randint(1000000, 9999999)
    # phonenumber = f"{random.choice(prefix)}{n}"

    phonenumber = f"{random.choice(prefix)}"
    for i in range(7):
        phonenumber += str(random.randint(0, 9))

    return phonenumber


def hamrahaval():
    prefix = ["0993", "0912", "0919", "0992"]

    # n = random.randint(1000000, 9999999)
    # phonenumber = f"{random.choice(prefix)}{n}"

    phonenumber = f"{random.choice(prefix)}"
    for i in range(7):
        phonenumber += str(random.randint(0, 9))

    return phonenumber


def rightell():
    prefix = ["0921", "0922", "0923"]

    # n = random.randint(1000000, 9999999)
    # phonenumber = f"{random.choice(prefix)}{n}"

    phonenumber = f"{random.choice(prefix)}"
    for i in range(7):
        phonenumber += str(random.randint(0, 9))

    return phonenumber
