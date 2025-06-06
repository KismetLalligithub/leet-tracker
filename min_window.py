from collections import Counter
def minWindow(s,t):
    if not t or not s: 
        return ""

    need = Counter(t)
    missing = len(t)
    l=best_l=0
    best_len= float('inf')

    for r, ch in enumerate(s):
        if need[ch] > 0: 
            missing -= 1 
        need_ch -= 1

        while missing == 0: 
            if r - l + 1 < best_len: 
                best_len, best_l = r - l + 1, l 

            left_ch = s[l]
            need[left_ch] += 1 
            if need[left_ch] > 0: 
                missing += 1 
            l += 1 

    return "" if best_len == float('inf') else s[best_l : best_l + best_len]
