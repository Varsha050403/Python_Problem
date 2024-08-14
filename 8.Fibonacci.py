def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))


number = int(input("Enter the number : "))
if number <= 0:
    print("Enter the positive number ")
else :
    for i in range(number):
        print(fibonacci(i),end=" ")