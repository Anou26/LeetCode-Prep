import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        min_heap = [(x*x + y*y, i) for i, (x, y) in enumerate(points)]
        heapq.heapify(min_heap)
        return [points[heapq.heappop(min_heap)[1]] for _ in range(k)]

        