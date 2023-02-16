class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ind = 0
        if target not in nums and target > nums[-1]:
            return len(nums)
        elif target not in nums and target < nums[0]:
            return 0
        elif target not in nums and target < nums[-1]:
            for i in range(len(nums)):
                if target > nums[i]:
                    ind = i+1
                else:
                    return ind
        else:
            return nums.index(target)