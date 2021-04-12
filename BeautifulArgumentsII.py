class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        result = []
        left, right = 1, n
        while left <= right:
            if k % 2:
                result.append(left)
                left += 1
            else:
                result.append(right)
                right -= 1
            if k > 1:
                k -= 1
        return result


