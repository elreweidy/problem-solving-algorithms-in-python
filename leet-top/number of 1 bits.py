class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n).replace("0b", '')
        bl = list(binary)
        res = 0
        for i in range(len(bl)):
            if bl[i] == '1':
                res += 1
        return res