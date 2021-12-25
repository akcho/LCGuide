# iterative
# time: O(n)
# space: O(n)
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

# recursive
# time: O(n)
# space: O(n)
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        else:
            return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]