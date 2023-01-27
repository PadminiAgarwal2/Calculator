x = int(input("Enter first number: "))
y = int(input("Enter second number: "))


def add(x, y):
    sum = x + y
    return sum


def subtract(x, y):
    if (x > y):
        difference = x - y
        return difference
    else:
        difference = y - x
        return difference


def multiply(x, y):
    product = x * y
    return product


def divide(x, y):
    quotient = (x / y)
    return quotient





print(add(x, y))
print(subtract(x, y))
print(multiply(x, y))
print(divide(x, y))
<<<<<<< HEAD:addition.py
=======
<<<<<<< HEAD


# Expontial power of any number
base = int(input("enter base value "))
exponent = int(input("enter exponent value "))
print("Exponential Value is: ", base ** exponent)

>>>>>>> a6d157a2fd65005f009bd88077a7f9284072b234:mathematical_operations.py

