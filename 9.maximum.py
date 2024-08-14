def maximum():
    number1 = int(input("Enter a number : "))
    number2 = int(input("Enter a number : "))
    number3 = int(input("Enter a number : "))
    if (number1 > number2) and (number1 > number3):
        print(f"{number1} is a greatest number")
    elif (number2 > number1) and (number2 > number3):
        print(f"{number2} is a greatest number")
    else:
        print(f"{number3} is a greatest number")

maximum()