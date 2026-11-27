class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n # standard habit 
        prices[src] = 0 # First node has to be zero because that will be the starting point. 

        for i in range(k + 1):
            tmpPrices = prices.copy() #Everything first gets updated in copy. 

            for s, d, p in flights:  # s = source, command d = destination, p = price 
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        return -1 if prices[dst] == float("inf") else prices[dst]