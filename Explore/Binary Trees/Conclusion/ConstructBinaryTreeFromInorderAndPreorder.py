# time: O(n)
# space: O(n)

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        preorder_idx = 0

        def helper(inorder_left, inorder_right):
            if inorder_left > inorder_right:
                return None

            nonlocal preorder_idx
            val = preorder[preorder_idx]
            root = TreeNode(val)
            preorder_idx += 1

            root.left = helper(inorder_left, idx_map[val] - 1)
            root.right = helper(idx_map[val] + 1, inorder_right)

            return root

        return helper(0, len(inorder) - 1)