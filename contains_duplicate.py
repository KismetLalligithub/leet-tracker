def contains_duplicate(nums): 
    seen = set(nums)
    
    if len(seen) != len(nums): 
        return True
    return False

