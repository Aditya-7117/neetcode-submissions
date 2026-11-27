class Solution:                 # O(n)
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): # Edge case 
            return -1

        total = 0
        res = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i] # Keep on calculating the difference

            if total < 0:
                total = 0
                res = i + 1
                
        return res
        