class Solution:
    def isValid(self, s: str) -> bool:

        stack, parenthese = [], {"(": ")", "{": "}", "[": "]"}

        for c in s:
            if c in parenthese:
                stack.append(c)

            elif len(stack) == 0 or parenthese[stack.pop()] != c:
                return False

        return len(stack) == 0

