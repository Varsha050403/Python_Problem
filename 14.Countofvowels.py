string = input().lower()
a = string.replace(" ","")
vowel_count = 0
constant_count = 0
for i in string:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vowel_count += 1
    else:
        constant_count += 1

print(vowel_count)
print(constant_count)