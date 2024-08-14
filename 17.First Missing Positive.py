def firstMissingPositive(nums):
    lst = []
    for i in range(1, len(nums) + 1):
        if i not in nums:
            lst.append(i)

    return min(lst)

nums = list(map(int,input().split()))
print(firstMissingPositive(nums))
