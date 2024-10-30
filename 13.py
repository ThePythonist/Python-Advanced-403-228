def factorial(x):
    if x == 1:
        return x
    else:
        return x * factorial(x - 1)


entry = int(input("Enter any number : "))

if entry > 0:
    print(f"Factorial of {entry} is {factorial(entry)}")
elif entry == 0:
    print("Factorial of 0 is 1")
else:
    print("Factorial doesnt exists")
