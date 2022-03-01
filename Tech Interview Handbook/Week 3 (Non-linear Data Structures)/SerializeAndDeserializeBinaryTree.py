# Recursive DFS
# time: O(n)
# space: O(n)
class Codec:
    def serialize(self, root):
        output = []
        def dfs(root):
            if not root:
                output.append("None,")
                return
            output.append(str(root.val) + ",")
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return "".join(output)

    def deserialize(self, data):
        data_list = data.split(",")
        data_q = deque(data_list)
        def dfs(q):
            val = q.popleft()
            if val == "None": return None
            root = TreeNode(val)
            root.left = dfs(q)
            root.right = dfs(q)
            return root
        return dfs(data_q)