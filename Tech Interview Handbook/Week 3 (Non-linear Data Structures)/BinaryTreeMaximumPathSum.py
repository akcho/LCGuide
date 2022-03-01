# Recursive DFS
# time: O(n)
# space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(root):
            nonlocal res
            if not root: return 0

            # find maxes of each side (0 to address negative max)
            left_max = max(dfs(root.left), 0)
            right_max = max(dfs(root.right), 0)

            # compute max path sum WITH split
            res = max(res, root.val + left_max + right_max)

            # return max path sum without split (WITH split is stored in res)
            return root.val + max(left_max, right_max)

        dfs(root)
        return res
