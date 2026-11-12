class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n + 1,...]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2 #Shift to one spot ahead, obviously. 
            rob2 = temp   #Same
        return rob2