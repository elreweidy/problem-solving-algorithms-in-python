class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums) == 1 and nums[0] == 0:
            return 1
        elif len(nums) == 1 and nums[0] > 0:
            return nums[0] - 1

        nums = sorted(nums)
        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] != 1:
                return nums[i+1] - 1
            elif nums[i+1] == nums[-1] and nums[i+1] - nums[i] == 1 and nums[0] != 1:
                return nums[-1] + 1
            elif nums[i+1] == nums[-1] and nums[i+1] - nums[i] == 1 and nums[0] == 1:
                return 0