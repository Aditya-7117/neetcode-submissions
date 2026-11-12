class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # This is all done for creating an adjacency list. 
        N = len(points)
        
        adj = {i:[] for i in range(N)} # Cost/distance, node 
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # Prim's
        res = 0
        visit = set()
        minHeap = [[0, 0]] #Cost, node 

        while len(visit) < N:
            cost, i = heapq.heappop(minHeap)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minHeap, [neiCost, nei])
        return res