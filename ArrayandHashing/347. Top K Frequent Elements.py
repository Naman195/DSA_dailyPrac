nums = [1,1,1,2,2,3]
k = 2

from heapq import *

def topK(nums, k):
    maxHeap = []
    mp = {}
    for num in nums:
        mp[num] = mp.get(num, 0) + 1
    for key, val in mp.items():
        heappush(maxHeap, (-val, key))
        
    
    ans = []
    
    for i in range(k):
        val, key = heappop(maxHeap)
        ans.append(key)
    print(ans)

topK(nums, k)        