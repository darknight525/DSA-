class Solution(object):
    def topKFrequent(self, nums, k):
        from collections import Counter
        import heapq
        
        freq = Counter(nums)   
        heap = []
        
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for count, num in heap]
        
