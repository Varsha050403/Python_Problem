def palindrome():
    n = int(input("Enter a number : "))
    numstr = str(n)
    a = ''.join(reversed(numstr))
    return a

print(palindrome())
