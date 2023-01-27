def add(x, y):
    sum = x + y
    return sum


def subtract(x, y):
        difference = x - y


def multiply(x, y):
    product = x * y
    return product
def divide(x,y):
    quotient =x/y
    return quotient



print("Select operator")
print("1.Add")
print("2.Subract")
print("3.multiply")
print("4.Divide")

if choice in ('1','2','3','4'):
    try:
        n=float(input("Enter first value:"))
        n1=float(input("Enter second value:"))
    except valueError:
        print("Invalid input.Please enter a no.")
        continue

    if choice =='1':
        print(n,"+",n1,"=",add(n,n1))
    elif choice =='2':
        print(n,"-",n1,"=", subtract(n,n1))
    elif choice =='3':
        print(n,"*",n1,"=",multiply(n,n1))
    elif choice =='4':
        print(n,"/",n1,divide(n,n1))
        break
else:
    print("Invalid input")




print(add(x, y))
print(subtract(x, y))
print(multiply(x, y))
print(divide(x, y))


# Expontial power of any number
base = int(input("enter base value "))
exponent = int(input("enter exponent value "))
print("Exponential Value is: ", base ** exponent)

# Factorial no.
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