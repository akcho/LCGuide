# time: O(n)
# space: O(n)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def LCA(root):
            if not root or (root in (p, q)):
                return root
            left = LCA(root.left)
            right = LCA(root.right)
            if left and right:
                return root
            return left or right  # only possible bc p and q HAVE to be in root
        return LCA(root)