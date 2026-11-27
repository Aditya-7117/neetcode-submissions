class Solution:
    def reorganizeString(self, s: str) -> str:
        res = ""
        count = Counter(s) #hash map 
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        prev = None # This stores the value to pause on for one turn/ to avoid repetition. 
        while maxHeap or prev:
            if prev and not maxHeap: # to prevent  "aa" situation 
                return ""
            # most frequent one, except prev
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
                
            if cnt != 0:
                prev = [cnt, char]
        return res
