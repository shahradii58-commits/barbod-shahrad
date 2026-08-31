print("=== easycale ===")

num1 = float(input("first number: "))
num2 = int(input("second number: "))

op = input("choose(+, -, *, /: )")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 -  num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("cannot divide by zero")
else:
    print("invalid operation")