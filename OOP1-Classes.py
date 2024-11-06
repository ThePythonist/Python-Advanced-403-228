import time


class Car:
    def __init__(self, name, color, hp, delay):
        self.name = name
        self.color = color
        self.horsepower = hp
        self.engine = False
        self.speed = 0
        self.delay = delay

    def start_engine(self):
        self.engine = True
        print(f"{self.name} : Started Engine")

    def accelerate(self, value):
        if self.engine == True:
            for i in range(value):
                print(f"{self.name} : Current speed is {self.speed}")
                time.sleep(self.delay / 10)
                self.speed += 10
        else:
            print("Engine is off")

    def brake(self):
        print("Braking")


# Instance(Nemone) - Object(Shey)

persia = Car("persia", "white", 100, 11)
runna = Car("runna", "black", 105, 12)
dena = Car("dena", "red", 115, 13.5)

persia.start_engine()
persia.accelerate(3)
