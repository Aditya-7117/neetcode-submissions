class Solution:
    def reorganizeString(self, s: str) -> str:
        res = ""
        count = Counter(s)

        # Negative frequencies to simulate a max heap
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        # Hold the last used character outside the heap for one turn
        prev = None

        while maxHeap or prev:
            # Only the previous character remains: repetition is unavoidable
            if prev and not maxHeap:
                return ""

            # Pick the most frequent available character (excluding prev)
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1  # Reduce remaining frequency (negative count)

            # Release OLD character only AFTER picking a different one
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            # Put CURRENT character on hold if occurrences remain
            if cnt != 0:
                prev = [cnt, char]

        return res