class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums) #Not zero, because input can be negative as well. 
        curMin, curMax = 1, 1 #Not zero because multiplying nums * 0 = 0

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            tmp = curMax * n   # Used because the curMin below will otherwise use the contaminated newly updated curMax. 
            curMax = max(n * curMax, n * curMin, n) # N, as only n can also be greater than the cur max or cur min 
            curMin = min(tmp, n * curMin, n) 
            res = max(res, curMax)
        return res


