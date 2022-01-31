# Approach 1: Depth First Search
# space: O(n+m)
# time: O(n)

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""


class Solution:
    def __init__(self):
        self.copied = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        copied = self.copied

        if not node: return None
        if node in copied: return copied[node]

        copied[node] = Node(node.val, [])

        if node.neighbors:
            copied[node].neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return copied[node]


# Approach 2: Breadth First Search
# space: O(n+m)
# time: O(n)

from collections import deque
class Solution2(object):

    def cloneGraph(self, node):
        if not node:
            return node

        copied = {}

        queue = deque([node])
        copied[node] = Node(node.val, [])

        while queue:
            popped_node = queue.popleft()
            for neighbor in popped_node.neighbors:
                if neighbor not in copied:
                    copied[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                copied[popped_node].neighbors.append(copied[neighbor])
        return copied[node]