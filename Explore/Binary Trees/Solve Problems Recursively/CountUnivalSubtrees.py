# time: O(n)
# space: O(H)
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.count = 0
        self.isUni(root)
        return self.count

    def isUni(self, node):
        if not node.left and not node.right:
            self.count += 1
            return True

        is_uni_left = True
        is_uni_right = True
        if node.left:
            is_uni_left = self.isUni(node.left) and node.left.val == node.val
        if node.right:
            is_uni_right = self.isUni(node.right) and node.right.val == node.val

        is_uni = is_uni_left and is_uni_right

        if is_uni:
            self.count += 1

        return is_uni

