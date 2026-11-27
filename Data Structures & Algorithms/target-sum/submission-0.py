class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} # (index, cursum) ->  num of ways

        def backtrack(i, cursum):
            # cache
            if (i, cursum) in dp: 
                return dp[(i, cursum)]
            # base case
            if i == len(nums):
                return 1 if cursum == target else 0
            # recursion
            dp[(i, cursum)] = (
                backtrack(i + 1, cursum + nums[i]) +
                backtrack(i + 1, cursum - nums[i])
            )
            return dp[(i, cursum)]
        return backtrack(0 , 0)
