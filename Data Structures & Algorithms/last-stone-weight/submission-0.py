class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = abs(heapq.heappop(stones))
            second = abs(heapq.heappop(stones))

            if second < first:
                heapq.heappush(stones, -(first - second)) #- as our list is negative 
        stones.append(0)
        return abs(stones[0]) 


