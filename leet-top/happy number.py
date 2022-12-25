import time
class Solution:
    def isHappy(self, n: int) -> bool:
        timeout = time.time() + 0.00002
        res = list(str(n))
        sq = 0
        while time.time() < timeout:
            if sq == 1:
                return True
            sq = 0
            for i in range(len(res)):
                sq += int(res[i]) ** 2
            res = list(str(sq))
        return False