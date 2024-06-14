# Write a program to check the number is a armstrong number or not.

def armstrong():
    n = int(input("Enter the number : "))
    size = len(str(n))
    armstrong_done = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        armstrong_done += digit ** size
        temp = temp // 10
    print(armstrong_done)
    if n == armstrong_done:
        print(f"{n} is a Armstrong number")
    else:
        print("Not a Armstrong number")


armstrong()
