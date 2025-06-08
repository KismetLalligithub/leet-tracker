def subarraySum(nums, k): 
    pref = 0 
    ans = 0 
    seen = defaultdict(int)
    seen[0] = 1 

    for num in nums: 
        pref += num
        ans += seen[pref - k] 
        seen[pref] += 1 
    return ans
