class Solution(object):
    def isValid(self, s):
        stack = []  # Create an empty stack to store opening brackets
        bracket_pairs = {')': '(', '}': '{', ']': '['}  # Define bracket pairs for faster lookup

        for c in s:
            if c in '([{':
                stack.append(c)
            elif c in bracket_pairs:
                if not stack or stack[-1] != bracket_pairs[c]:
                    return False
                stack.pop()

        return not stack


