class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.defaultdict(int)
        for n in nums:
            freq[n] += 1
        
        minHeap = []

        for num, count in freq.items():
            heapq.heappush(minHeap, (count, num))

            if len(minHeap) > k:
                heapq.heappop(minHeap)

        res = []
        for count, num in minHeap:
            res.append(num)
        
        return res

