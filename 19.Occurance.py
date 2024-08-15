def occurance(string):
    s = string.replace(" ", "")
   # s = "".join(string)  --- for list as an input
    dic = {}
    for i in s:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    return dic


string = input()
print(occurance(string))
