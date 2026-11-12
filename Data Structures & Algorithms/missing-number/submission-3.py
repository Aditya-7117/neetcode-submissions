class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = n

        for i, v in enumerate(nums):
            res = res ^ i ^ v
        return res 