import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_c = collections.Counter(nums)
        for i in range(len(nums)):
            if nums_c[nums[i]] > (len(nums) // 2):
                return nums[i]