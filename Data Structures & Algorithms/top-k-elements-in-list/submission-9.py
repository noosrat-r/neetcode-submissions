class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] = count[n] + 1
        
        minHeap = []
        for value, count in count.items():
            heapq.heappush(minHeap, [count,value])

            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        res = []
        while minHeap:
            res.append(heapq.heappop(minHeap)[1])
        
        return res
