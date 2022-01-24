# basic stack
# time: O(n)
# space: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "}": "{", "]": "["}

        stack = []

        for b in s:
            # if bracket is in pairs (ie. bracket is a cb key):
            # closed_bracket = bracket
            # open_bracket = pairs[closed_bracket]
            if b in pairs:
                cb = b
                ob = pairs[cb]

                seen = stack.pop() if stack else -1
                if seen != ob:
                    return False
            else:
                ob = b
                stack.append(ob)

        return not stack

