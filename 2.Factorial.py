def factorial(a):

    if a == 1:
        return a
    else:
        return a * factorial(a - 1)


a = int(input("Enter a: "))
print(factorial(a))