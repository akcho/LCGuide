# time: O(n)
# space: O(n) >- store the entire tree
class Solution:
    def buildTree(self, inorder, postorder):
        idx_map = {val: idx for idx, val in enumerate(inorder)}

        def helper(inorder_left, inorder_right):
            if inorder_left > inorder_right:
                return None

            val = postorder.pop()
            root = TreeNode(val)

            root_idx = idx_map[val]

            root.right = helper(root_idx + 1, idx_right) # right tree
            root.left = helper(idx_left, root_idx - 1) # left tree

            return root

        return helper(0, len(inorder) - 1) # entire tree