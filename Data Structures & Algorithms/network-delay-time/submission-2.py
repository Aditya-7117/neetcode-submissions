class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)

        for node, nei, wt in times:
            edges[node].append([nei, wt])
        
        visit = set()
        minHeap = [(0, k)]
        time = 0
        while minHeap:
            w1, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            
            visit.add(node)
            time = max(time, w1)

            for nei, w2 in edges[node]:
                if nei not in visit: 
                    heapq.heappush(minHeap, (w1 + w2, nei))
        return time if len(visit) == n else -1

