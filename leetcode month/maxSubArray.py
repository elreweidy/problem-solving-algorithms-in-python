class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_checked = total_sum = nums[0]

        for i in range(1, len(nums)):
            max_checked = max(nums[i], nums[i] + max_checked)
            total_sum = max(total_sum, max_checked)

        return total_sum