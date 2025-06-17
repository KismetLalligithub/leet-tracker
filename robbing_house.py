def robbingHouses(nums): 
    if not nums: 
        return 0
    if len(nums) < 3: 
        return max(nums)
    
    prev1, prev2 = 0, 0 

    for i in range(len(nums)): 
        temp = max(prev1, prev2 + num)
        prev2 = prev1 
        prev1 = temp

    return prev1 
