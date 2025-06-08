def productExceptSelf(nums): 
    n = len(nums)
    out = [1] * n 

    pref = 1 
    for i in range(n): 
        out[i] = pref
        pref *= nums[i]

    suff = 1 

    for i in range(n - 1, -1, -1): 
        out[i] *= suff
        suff *= nums[i]
    
    return out
