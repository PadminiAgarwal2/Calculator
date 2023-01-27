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
5

# Expontial power of any number
base = int(input("enter base value "))
exponent = int(input("enter exponent value "))
print("Exponential Value is: ", base ** exponent)


n=int(input("Enter value:"))
fact=1
if n<0:
    print("sorry factorial does not exit")
elif n==0:
    print("The factorial of 0 and 1")
else:
    for i in range(1,n+1):
      fact=fact*i
      print("The factorial of",n,"is",fact)

# radian to degree code
pi=22/7
radian = float(input("Input radians: "))
degree = radian*(180/pi)
print(degree)
      