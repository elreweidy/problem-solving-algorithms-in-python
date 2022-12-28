class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            maxArea = (r-l) * min(height[l], height[r])
            print(maxArea)
            if height[r] == height[l]:
                l += 1
            elif height[l] > height[r]:
                r-= 1
            elif height[r] > height[l]:
                l+=1
            if maxArea> res:
                res = maxArea
        return res