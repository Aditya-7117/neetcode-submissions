class Solution:                                     # O(n)
    def rob(self, nums: List[int]) -> int:
        
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    

    def helper(self, nums): # house robber 1 helper
        rob1, rob2 = 0, 0 # max amount u can rob from prev 2 houses

        for n in nums:
            newRob = max(n + rob1, rob2) # Assuming [rob 1, rob 2, n ] is the order 
            rob1 = rob2   # Shifting both pointers. 
            rob2 = newRob
        return rob2