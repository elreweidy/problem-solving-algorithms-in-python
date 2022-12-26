class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zeros = []
        for i in range(len(nums)):
            if nums[i] != 0:
                non_zeros.append(i)

        for i in range(len(non_zeros)):
            if i != non_zeros[i]:
                nums[i], nums[non_zeros[i]] = nums[non_zeros[i]], 0