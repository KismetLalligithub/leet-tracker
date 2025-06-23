import heapq
from collections import Counter 

def k_th_largest(nums, k): 
    nums.sort()
    return nums[len(nums) - k]

# other solution
def topKFrequent(nums, k): 
    count = Counter(nums)

    heap = []

    for num, freq in count.items(): 
        heapq.heappush(heap, (freq, num))
        if len(heap) > k: 
            heapq.heappop(heap)

    return [num for freq, num in heap]

def topKFrequent_optimized(nums, k): 
    count = Counter(nums)
   
   buckets = [[] for _ in range(len(nums) + 1)]

   for num, freq in count.items(): 
       for num in buckets[i]: 
           result.append(num)
           if len(result) == k: 
               return result
    return result
# ^ code does not work

def kth_largest(nums, k): 
    return heapq.nlargest(k, nums)[-1]

