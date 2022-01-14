# stack
# time: O(n)
# space: O(n)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }
        stack = []

        for t in tokens:
            if t not in operations:
                stack.append(int(t))
            else:
                n2 = stack.pop()
                n1 = stack.pop()
                operation = operations[t]
                stack.append(operation(n1, n2))
        return stack.pop()