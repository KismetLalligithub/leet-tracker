
def threesum(nums): 
    n = len(nums)
    nums.sort()
    solutions = []

    for i in range(len(nums) - 2): 
        if i > 0 and nums[i] == nums[i - 1]: 
            continue
        
        l, r = i + 1, n - 1
        target = -nums[i]

        while l < r: 
            curr_sum = nums[l] + nums[r]

            if curr_sum == target: 
                solutions.append([nums[i], nums[l], nums[r]])

                while l < r and nums[l] == nums[l + 1]: 
                    l += 1 
                while l < r and nums[r] == nums[r - 1]: 
                    r -= 1

                l += 1 
                r -= 1 
            elif curr_sum < target: 
                l += 1
            else: 
                r -= 1
    
    return solutions
