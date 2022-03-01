# Approach 1: Neetcode's DFS
# time: O(n)
# space:O(n+m)
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        old_to_new = {}

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]

            copy = Node(node.val)
            old_to_new[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None


# Approach 2: Depth First Search
# space: O(n+m)
# time: O(n)

class Solution:
    def __init__(self):
        self.copied = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        copied = self.copied

        if not node:
            return None
        elif node in copied:
            return copied[node]
        else:
            copied[node] = Node(node.val, [])
            if node.neighbors:
                copied[node].neighbors = [self.cloneGraph(n) for n in node.neighbors]
            return copied[node]


# Approach 3: Breadth First Search
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