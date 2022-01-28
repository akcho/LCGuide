# Recursive Traversal with Valid Range
# time: O(n)
# space: O(n)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            # Empty trees are still BSTs
            if not node:
                return True

            if node.val <= low or node.val >= high:
                return False

            validate_right = validate(node.right, node.val, high)
            validate_left = validate(node.left, low, node.val)

            return validate_left and validate_right

        return validate(root, float("-inf"), float("inf"))


# Iterative Inorder Traversal
# time: O(n)
# space: O(n)
class Solution2:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True

        stack = []
        curr = root
        prev = None

        while curr or stack:
            # add all left currs to stack and traverse to leftmost node
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            # in a BST, prev will ALWAYS be less than curr bc we traverse left first
            if prev and prev.val >= curr.val:
                return False

            prev = curr
            curr = curr.right
        return True