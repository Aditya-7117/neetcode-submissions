class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0
        while l < r:
            if heights[l] >= heights[r]:
                water = (r - l) * heights[r]
                res = max(res, water)
                r -= 1
            else:
                water = (r - l) * heights[l]
                res = max(res, water)
                l += 1
        return res
            