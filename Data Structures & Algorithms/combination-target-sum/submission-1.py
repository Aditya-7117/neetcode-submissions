class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total): #index, current combination, total 
            #Base cases 
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            # Check more combinations if base case not yet satisfied 
            cur.append(nums[i])
            dfs(i, cur, total + nums[i]) # Call dfs on left branch that we include 
            cur.pop()
            dfs(i + 1, cur, total) #Call DFS on the right branch that we exclude the number. Therefore, trying out on the next index, i + 1. 
        dfs(0, [], 0)
        return res