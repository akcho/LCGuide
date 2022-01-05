# Approach 1: Queue
# time: O(n)
# space: O(n)
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        Q = collections.deque([root])
        while Q:
            lvl_size = len(Q)
            for i in range(lvl_size):
                node = Q.popleft()

                # This check is important. We don't want to
                # establish any wrong connections. The queue will
                # contain nodes from 2 levels at most at any
                # point in time. This check ensures we only
                # don't establish next pointers beyond the end
                # of a level
                if i < size - 1:
                    node.next = Q[0]

                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)

        return root


# Approach 2: Linked List
# time: O(n)
# space: O(1)
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def setChild(childNode, prev, leftmost):
            if childNode:
                if not prev:  # first child in level
                    leftmost = childNode
                else:  # already found a left child via this func
                    prev.next = childNode
                prev = childNode
            return prev, leftmost

        if not root:
            return root
        leftmost = root
        while leftmost:
            prev, curr = None, leftmost
            leftmost = None
            while curr:
                prev, leftmost = setChild(curr.left, prev, leftmost)
                prev, leftmost = setChild(curr.right, prev, leftmost)
                curr = curr.next
        return root