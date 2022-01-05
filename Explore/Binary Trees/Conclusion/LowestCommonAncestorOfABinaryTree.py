# time: O(n)
# space: O(n)
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def LCA(root):
            if root is None or root in (p, q):
                return root
            left = LCA(root.left)
            right = LCA(root.right)
            if left and right:
                return root
            else:  # one of them is null, so return the good one
                return left or right
        return LCA(root)