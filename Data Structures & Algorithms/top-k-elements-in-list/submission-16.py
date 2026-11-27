class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1
        
        maxHeap = []
        for num, count in freq.items():
            heapq.heappush(maxHeap, (count, num))

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
            
        res = []
        for count, num in maxHeap:
            res.append(num)
        return res
        
        