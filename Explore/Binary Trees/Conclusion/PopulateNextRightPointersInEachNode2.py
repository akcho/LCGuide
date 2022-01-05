# Approach 1: Queue
# time: O(n)
# space: O(n)
class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return root

        # Initialize a queue data structure which contains
        # just the root of the tree
        Q = collections.deque([root])

        # Outer while loop which iterates over
        # each level
        while Q:

            # Note the size of the queue
            size = len(Q)

            # Iterate over all the nodes on the current level
            for i in range(size):

                # Pop a node from the front of the queue
                node = Q.popleft()

                # This check is important. We don't want to
                # establish any wrong connections. The queue will
                # contain nodes from 2 levels at most at any
                # point in time. This check ensures we only
                # don't establish next pointers beyond the end
                # of a level
                if i < size - 1:
                    node.next = Q[0]

                # Add the children, if any, to the back of
                # the queue
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)

        # Since the tree has now been modified, return the root node
        return root

# Approach 2: Linked List
# time: O(n)
# space: O(1)
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def setChild(childNode, prev, leftmost):
            if childNode:
                if prev:
                    prev.next = childNode
                else:  # we've already found a left child node
                    leftmost = childNode
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