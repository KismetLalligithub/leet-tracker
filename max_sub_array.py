from itertools import accumulate

def maxSubArray(nums): 
    prefix = list(accumulate(nums))
    best = prefix[0]
    min_pref = 0 

    for p in prefix: 
        best = max(best, p - min_pref)
        min_pref = min(min_pref, p)
    return best
