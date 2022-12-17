class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sums = 0
        accum = len(digits)
        for i in range(len(digits)):
            sums += digits[i] * pow(10, accum)
            accum -= 1
        sums = (sums // 10) + 1
        sum_l = list(str(sums))

        return [int(i) for i in sum_l]