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

            if stack[-1].right:
                left_node = stack[-1].right
            else:
                curr = stack.pop()
                output.append(curr.val)
                while stack and stack[-1].right == curr:  # next stack node considers curr its right node
                    curr = stack.pop()
                    output.append(curr.val)
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