import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
    
    # Use a heap to find the k most frequent elements
        return heapq.nlargest(k, count.keys(), key=count.get)
        