class BankAccount:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.balance = 0

    def withdraw(self, value):  # bardasht
        if self.balance >= value + 10:
            self.balance -= value
            print(f"Decreased balance : {value}")
            print("-" * 50)
            self.showbalance()
        else:
            print("Not enough credit")
            print("-" * 50)

    def deposit(self, value):  # variz
        self.balance += value
        print(f"Increased balance : {value}$")
        print("-"*50)
        self.showbalance()

    def showbalance(self):
        print(f"Current account balance : {self.balance}$")
        print("-"*50)


user1 = BankAccount("alireza", "1001")
user2 = BankAccount("kiana", "1001")

user1.deposit(500)
user1.deposit(500)

user1.withdraw(200)
