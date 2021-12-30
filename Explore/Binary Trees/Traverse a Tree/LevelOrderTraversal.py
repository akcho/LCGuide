# Approach 1: Recursion
# time: O(n)
# space: O(n)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        levels = []

        def helper(root, level):
            if len(levels) == level:
                levels.append([])
            levels[level].append(root.val)

            if root.left:
                helper(root.left, level + 1)
            if root.right:
                helper(root.right, level + 1)

        helper(root, 0)
        return levels


# Approach 2: Iterative
# time: O(n)
# space: O(n)
class Solution2:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        output = []
        level = 0
        queue = deque([root])
        while queue:
            output.append([])
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()
                output[level].append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1
        return output