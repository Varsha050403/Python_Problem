def sum_of_digits():
    number = int(input("Enter the number : "))
    temp = number
    sum = 0
    while temp > 0:
        n = temp % 10
        sum += n
        temp //= 10
    print(sum)


sum_of_digits()
