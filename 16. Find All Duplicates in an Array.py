def findDuplicates(nums):
    non_dup = []
    dup = []
    for i in range(0, len(nums)):
        if nums[i] not in non_dup:
            non_dup.append(nums[i])
        else:
            dup.append(nums[i])

    return dup

nums = list(map(int,input().split()))
print(findDuplicates(nums))