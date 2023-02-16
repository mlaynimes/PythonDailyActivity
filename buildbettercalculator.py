num1 = float(input("Enter the First Number: "))
op = input("Enter operator like +, - , / or *: ")
num2 = float(input("Enter the Second Number: "))


if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("please follow the instruction")