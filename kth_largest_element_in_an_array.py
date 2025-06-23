import heapq
from collections import Counter 

def kth_largest(nums, k): 
    nums.sort()
    return nums[len(nums) - k]

# other solution: one liner

def kth_largest(nums,k):
    return heapq.nlargest(k, nums)[-1]

