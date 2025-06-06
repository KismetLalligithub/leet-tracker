def pivotIndex(nums):
    n = len(nums)
    prefix_s = [0] * n

    for i in range(n): 
        if i == 0: 
            prefix_s[i] = nums[i]
        else: 
            prefix_s[i] = prefix_s[i - 1] + nums[i]

    for i in range(n): 
        if i == 0:
            if 0 == perfix_s[n - 1] - prefix_s[i]: 
                return 0
        elif prefix_s[i - 1] == prefix_s[n - 1] - prefix_s[i]: 
            return i 
    return -1

#one pass solution
def pivotIndex(nums): 
    total = sum(nums)
    left = 0
    
    for i, x in enumerate(nums): 
        if left == total - left - x: 
            return i
        left += x 
    return -1
