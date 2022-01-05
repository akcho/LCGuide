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
        return "".join(res)

    def deserialize(self, data):
        def dfs(str_q):
            if str_q[0] == "None":
                str_q.popleft()
                return None
            root = TreeNode(str_q[0])
            str_q.popleft()
            root.left = dfs(str_q)
            root.right = dfs(str_q)
            return root

        data_list = data.split(',')
        data_q = deque(data_list)
        root = dfs(data_q)
        return root

