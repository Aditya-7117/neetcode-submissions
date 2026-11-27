
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        # Reverse sort so pop() gives the smallest destination in lexical order 
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)

        res = []

        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()  # Consume this ticket once
                dfs(dst)

            # Add the airport only after using its outgoing tickets.
            res.append(src)

        dfs("JFK")
        return res[::-1]
