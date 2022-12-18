class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        sums = 0
        vals = []
        if n > 2:
            vals.append(1)
            vals.append(2)
            for i in range(2,n):
                sums = vals[-1] + vals[-2]
                vals.append(sums)

        return sums