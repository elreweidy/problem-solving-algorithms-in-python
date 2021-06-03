class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1: return 1

        f = [None for _ in range(2)]

        f[0] = 1
        f[1] = 2

        for _ in range(2, n):
            new = f[0] + f[1]
            f[0], f[1] = f[1], new

        return f[1]