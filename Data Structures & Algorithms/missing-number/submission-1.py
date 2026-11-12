class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hashset = set(range(len(nums) + 1))
        return (hashset - set(nums)).pop()