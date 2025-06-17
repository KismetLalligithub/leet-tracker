def robbingHouses(nums): 
    l1, l2, sum1, sum2 = 0, 1, 0, 0 

    while l1 < len(nums) and l2 < len(nums): 
        sum1 += nums[l1]
        sum2 += nums[l2]
        l1 += 2 
        l2 += 2

    if l1 < len(nums): 
        sum1 += nums[l1]
    if l2 < len(nums): 
        sum2 += nums[l2]

    return max(sum1, sum2)

print(robbingHouses([1, 2, 3, 4]))
