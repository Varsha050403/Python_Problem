def findDisappearedNumbers(nums):
    maxi = max(nums)
    fin = []
    for i in range(1, maxi+1):
        if i not in nums:
            fin.append(i)
    return fin
nums = list(map(int,input().split()))
print(findDisappearedNumbers(nums))