# iterative
# time: O(n)
# space: O(n)
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, output = [], []
        left_node = root

        while stack or left_node:
            while left_node:
                stack.append(left_node)
                left_node = left_node.left

            right_node = stack[-1].right
            if right_node:
                left_node = right_node
            else:
                node = stack.pop()
                output.append(node.val)
                while stack and stack[-1].right == node:
                    node = stack.pop()
                    output.append(node.val)
        return output

# recursive
# time: O(n)
# space: O(n)
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        else:
            return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]