def maxArea(height): 
    l = 0 
    r = len(height) - 1 
    max_area = float('-inf')

    while l < r: 
        max_area = max(max_area, min(height[l], height[r]) * (r - l))

        if height[l] < height[r]: 
            l += 1 
        else: 
            r -= 1
    
    return max_area
