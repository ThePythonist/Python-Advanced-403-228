class Person:
    def __init__(self, name, age, job, city):
        self.name = name
        self.age = age
        self.job = job
        self.city = city

    def talk(self):
        print(f"""
I'm {self.name} and I'm {self.age} years old.
I work as a {self.job} and I live in {self.city}.
        """)


hamed = Person("hamed kiani", 30, "backend developer", "isfahan")
mamad = Person("mohammad alizadeh", 27, "frontend developer", "rasht")

mamad.talk()

