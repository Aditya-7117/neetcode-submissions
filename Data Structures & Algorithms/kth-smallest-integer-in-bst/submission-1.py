# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0  # Once n == k, we can stop. 
        stack = []
        cur = root

        while cur or stack:
            while cur: # Keep going left and append it to the stack. 
                stack.append(cur)
                cur = cur.left

            cur = stack.pop() # Means we are processing this node officially. 
            n += 1
            if n == k:
                return cur.val
            cur = cur.right