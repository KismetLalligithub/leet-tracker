def lengthOfLongestSubstring(s): 
    if s == "": 
        return 0

    max_length = float('-inf')
    counter = []
    
    for r in range(len(s)): 
        while s[r] in counter: 
            if len(counter) == 1: 
                counter = []
            else: 
                counter = counter[1:]
            counter.append(s[r])
            max_length = max(max_length, len(counter))
    return max_length
            
