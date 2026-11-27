class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = defaultdict(int)
        for n in hand:
            count[n] += 1
        # We'll use a heap for faster minimum finding instead of finding from a hash map. 
        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0] # Minimum value 

            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]: #Basically, there is still a lower number. 
                        return False
                    heapq.heappop(minH)
        return True