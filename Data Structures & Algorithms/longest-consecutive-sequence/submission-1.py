class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)

        for n in nums:
            if (n - 1) not in numSet: # Means it is start of sequence
                length = 0
                while (n + length) in numSet: #Keep checking if consecutive numbers are there in that set. 
                    length += 1
                longest = max(length, longest)

        return longest