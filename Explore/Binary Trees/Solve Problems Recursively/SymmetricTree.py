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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque()
        q.append(root.left)
        q.append(root.right)

        while q:
            t1 = q.popleft()
            t2 = q.popleft()

            if not t1 and not t2:
                continue
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False

            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)
        return True