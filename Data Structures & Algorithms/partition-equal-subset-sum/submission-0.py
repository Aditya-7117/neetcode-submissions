class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0) # Base case added: if we don't choose any element, it remains 0.
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set() # Done so that there is no clash between first traversing set and also appending
            for t in dp:
                if (t + nums[i] == target):
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return True if target in dp else False