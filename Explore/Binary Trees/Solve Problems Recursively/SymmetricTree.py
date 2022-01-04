# Approach 1: Recursive
# time: O(n)
# space: O(n)
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root.left, root.right)

    def isMirror(self, t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return t1.val == t2.val and self.isMirror(t1.right, t2.left) and self.isMirror(t2.right, t1.left)

# Approach 2: Iterative
# time: O(n)
# space: O(n)
class Solution:
    def isSymmetric(self, root):
        if not root:
            return True

        q = collections.deque([root.left, root.right])

        while q:
            t1, t2 = q.popleft(), q.popleft()

            if not t1 and not t2:
                continue
            elif (not t1 or not t2) or (t1.val != t2.val):
                return False

            q += [t1.left, t2.right, t1.right, t2.left]

        return True