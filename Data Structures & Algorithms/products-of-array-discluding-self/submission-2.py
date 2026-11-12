class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) # Creating the list of positions equal to the length of the numbers 
        #Prefix
        prefix = 1
        for i in range(len(nums)):      
            res[i] = prefix
            prefix *= nums[i]

        #Postfix 
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *=postfix
            postfix *= nums[i]
        
        return res
