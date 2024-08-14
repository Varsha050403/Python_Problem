# Method 1 : Using Reversed method
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

# Method 2 : Using mathematical method
def pal():
    n = int(input())
    org = n
    reversed_number = 0
    while n > 0:
        reversed_number = reversed_number * 10 + n % 10
        n = n // 10
    if org == reversed_number:
        print(f"{org} id a palindrome number")
    else:
        print("Not a palindrome number")

pal()

# Method 3 : Using indexing

def method3():
    number = int(input("Enter the number : "))
    num = str(number)
    reverse = num[::-1]
    print(reverse)

method3()