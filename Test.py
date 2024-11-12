# class A:
#     def sayhello(self):
#         print("hello")
#
#
# class B(A):
#     def saygoodbye(self):
#         print("goodbye")
#
#
# valed = A()
# farzand = B()
#
# farzand.sayhello()


class Parent:
    def __init__(self, lastname, city, job):
        self.lastname = lastname
        self.city = city
        self.job = job

    def sayhello(self):
        print("hello")


class Child(Parent):
    def __init__(self, lastname, city, university, job=None):
        super().__init__(lastname, city, job)
        self.university = university

    def saygoodbye(self):
        print("goodbye")


valed = Parent("ahmadi", "yazd", "teacher")
farzand = Child("ahmadi", "tehran", "sharif", "engineer")

print(farzand.job)
