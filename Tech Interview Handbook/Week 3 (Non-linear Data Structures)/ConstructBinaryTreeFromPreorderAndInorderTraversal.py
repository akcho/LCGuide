# recursive dfs
# time: O(n)
# space: O(n)

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx_map = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = 0

        def helper(left, right):
            # base case: we've encountered a null node if left > right
            if left > right:
                return None

            nonlocal pre_idx
            root_val = preorder[pre_idx]
            # Remember that pre_idx goes root -> left-> right. We're recursing in that order.
            pre_idx += 1

            root = TreeNode(root_val)
            root_idx = inorder_idx_map[root_val]

            root.left = helper(left, root_idx - 1)  # root_idx-1 == rightmost node on the root's left subtree
            root.right = helper(root_idx + 1, right)  # root_idx+1 == leftmost node on the root's right subtree

            return root

        return helper(0, len(inorder) - 1)