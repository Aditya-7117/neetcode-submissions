class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd's algorithm 
        slow, fast = 0, 0 # Both initialized at 0 because the 0th position is never going to be part of the cycle. 
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Introducing a second slow pointer 
        slow2 =0 
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow