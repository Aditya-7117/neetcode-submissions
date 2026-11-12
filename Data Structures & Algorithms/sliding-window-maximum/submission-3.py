class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque() # index
        output = []
        l = r = 0

        while r < len(nums):
            #Popping smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            #Remove left value from window. 
            if l > q[0]:
                q.popleft()

            #Window  
            if r - l + 1 == k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output 