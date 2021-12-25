# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack, res = [], []
        curr = root

        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                node = stack[-1].right
                if not node:
                    node = stack.pop()
                    res.append(node.val)
                    while stack and stack[-1].right == node:
                        node = stack.pop()
                        res.append(node.val)
                else:
                    curr = node
        return res