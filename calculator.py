import math

a = int(input('Enter value of a: '))
b = int(input('Enter value of b: '))

# Addition


def Addition():
    sum = a + b
    print(sum)

# Subtraction
    def Subtract():
    result = num1 - num2
    print(Subtract)

# Multiplication


def multiply():
    result = int
    result = a*b
    print(result)

# Division


def divide(a, b):
    return a/b


print("Enter your choice: ")
print("a. Add")
print("b. Subtract")
print("c. Multiplication")
print("d. Division")

choice = input("Enter choice: ")

if choice == 'a':
    Addition()

elif choice == 'b':
    Subtract()

elif choice == 'c':
    Multiply()

elif choice == 'd':
    print("", divide(a, b))
else:
    print("Invalid choice")
