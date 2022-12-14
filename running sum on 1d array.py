class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = 0
        output = []
        for i in range(len(nums)):
            running_sum += nums[i]
            output.append(running_sum)
        return output