
# Simple Calculator

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
print("Choose operator : + , - , / , * ")
op = input("Enter Operator : ")

if op == "+":
    print('Result: ', a + b )
elif op == "-":
    print("Result: ", a - b )
elif op == "*":
    print("Result: ", a * b )
elif op == "/":
    if b != 0:
        print("Result: " ,  a / b)
    else:
        print("Not divisible by zero")
else:
    print("Invalid operator")

