class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            #Decision to include nums[i] (left branch)
            subset.append(nums[i])
            dfs(i + 1)

            #Decision to not include nums[i](right branch)
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res