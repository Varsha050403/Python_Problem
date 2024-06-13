def palindrome():
    n = int(input("Enter a number : "))
    num_string = str(n)
    a = ''.join(reversed(num_string))
    if a == num_string:
        print("Given number is palindrome")
    else:
        print("Not palindrome")
    return a


print(palindrome())
