# Approach 1: Iterative top-down
# time: O(n)
# space: O(log n)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []

        if root is not None:
            stack.append((1, root))

        depth = 0
        while stack:
            curr_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, curr_depth)
                stack.append((curr_depth + 1, root.left))
                stack.append((curr_depth + 1, root.right))

        return depth

# Approach 2: Recursive top-down
# time: O(n)
# space: O(log n)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0

        def helper(root, depth):
            if not root:
                return
            if not root.left and not root.right:
                self.max_depth = max(self.max_depth, depth)
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)

        helper(root, 1)
        return self.max_depth

# Approach 3: Recursive bottom-up
# time: O(n)
# space: O(log n)
class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            return max(left, right) + 1