def foursum(nums): 
    n = len(nums)
    nums.sort()
    solutions = []

    for i in range(n - 3): 
        if i > 0 and nums[i] == nums[i - 1]: 
            continue
        for  j in range(i + 1, n - 2): 
            if j > i + 1 and nums[j] == nums[j - 1]: 
                continue
            need = target - nums[i] - nums[j]
            l, r = j + 1, n - 1

            while l < r: 
                curr_sum = nums[l] + nums[r]
                if need = curr_sum: 
                    solutions.append([nums[i], nums[j], nums[l], nums[r]])

                    while l < r and nums[l] == nums[l + 1]: 
                        l += 1
                    while l < r and nums[r] == nums[r - 1]: 
                        r -= 1
                    l += 1
                    r -= 1
                elif curr_sum < need: 
                    l += 1
                else: 
                    r -= 1
    return solutions
