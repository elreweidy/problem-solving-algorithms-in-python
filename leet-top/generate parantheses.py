class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrace(opened, close):
            if opened == close == n:
                res.append("".join(stack))
            if opened < n:
                stack.append("(")
                backtrace(opened+1, close)
                stack.pop()
            if close < opened:
                stack.append(")")
                backtrace(opened, close+1)
                stack.pop()
        backtrace(0, 0)
        return res