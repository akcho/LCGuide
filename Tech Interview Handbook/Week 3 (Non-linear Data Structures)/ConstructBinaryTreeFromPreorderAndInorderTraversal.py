# recursive dfs
# time: O(n)
# space: O(n)

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = 0

        def helper(left, right):
            if left > right:
                return None

            nonlocal pre_idx
            val = preorder[pre_idx]
            pre_idx += 1

            root = TreeNode(val)
            root_idx = idx_map[val]

            root.left = helper(left, root_idx - 1)
            root.right = helper(root_idx + 1, right)

            return root

        return helper(0, len(inorder) - 1)