class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set(nums)

        if Counter(hashset) == Counter(nums):
            return False
        return True