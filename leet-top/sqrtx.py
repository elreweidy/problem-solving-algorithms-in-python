class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        start, end = 1, x
        while start <= end:
            mid = (start + end) // 2
            if mid * mid == x:
                return mid

            if mid * mid > x:
                end = mid - 1
            else:
                start = mid + 1
                res = mid
        return res