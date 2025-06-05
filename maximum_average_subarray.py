def findMaxAverage(nums): 
    best = float('-inf')
    curr = sum(nums[:k])

    for r in range(k, len(nums)): 
        curr += nums[r] - nums[r - k]
        best = max(best, curr)
    
    return best / k 

