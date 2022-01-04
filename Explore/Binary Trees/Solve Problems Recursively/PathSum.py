# Approach 1: Recursion
# time: O(n)
# space: O(log(n))
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        targetSum -= root.val

        if not root.left and not root.right:
            return targetSum == 0

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)


# Approach 2: Iteration (DFS)
# time: O(n)
# space (O(log(n))
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        stack = [(root, targetSum - root.val)]

        while stack:
            node, targetSum = stack.pop()
            if not node.right and not node.left and targetSum == 0:
                return True

            # node.right doesn't need to come before node.left
            if node.right:
                stack.append((node.right, targetSum - node.right.val))
            if node.left:
                stack.append((node.left, targetSum - node.left.val))
        return False