class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        largest = 0 
        
        for n in nums:
            if (n - 1) not in numset:
                length = 0
                while (length + n) in numset:
                    length += 1
                largest = max(largest, length)
        return largest