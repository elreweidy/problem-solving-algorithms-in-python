class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # hash table solution (which is better)

        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i
        return []

        # nested for loop solution (slow)

#         for i in range(len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
