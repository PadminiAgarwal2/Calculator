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

# Expontial power of any number
base = int(input("enter base value "))
exponent = int(input("enter exponent value "))
print("Exponential Value is: ", base ** exponent)

# Factorial no.
num = int(input("Enter a number for factorial:"))


def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1);


print("Factorial of", num, "is", factorial(num))

# Take input a number from user
num = int(input("Enter an any number: "))
cube = num * num * num
print("Cube of {0} is {1} ".format(num, cube))
