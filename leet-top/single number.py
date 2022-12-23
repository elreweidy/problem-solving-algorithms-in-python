import collections
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums_c = collections.Counter(nums)
        for i in range(len(nums)):
            if nums_c[nums[i]] == 1:
                return nums[i]