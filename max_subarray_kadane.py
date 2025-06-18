def max_subarray_kadane(nums): 
    best = curr = nums[0]

    for i in range(1, len(nums)): 
        curr = max(nums[i], curr + nums[i + 1])
        best = max(best, curr)
    
    return best
