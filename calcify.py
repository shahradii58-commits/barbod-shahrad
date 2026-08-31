number_1 = int(input("enter your int number : "))
number_2 = int(input("enter your  number : "))
arithmetical = input("choose(+, -, *, /: )")
if arithmetical == "+":
    print(number_1+number_2)
elif arithmetical == "*":
    print(number_1*number_2)
elif arithmetical == "-":
    print(number_1-number_2)
elif arithmetical == "/":
    if number_2 != 0:
        print(number_1/number_2)
    else:
        print("invalid choice")
        



