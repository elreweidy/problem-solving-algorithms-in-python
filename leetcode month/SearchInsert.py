import numpy as np


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if target > nums[-1]:
            return len(nums)
        for i, item in enumerate(nums):

            if item == target:
                return i
                break
            elif item > target:
                return i
                break
