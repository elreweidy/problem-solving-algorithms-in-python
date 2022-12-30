import collections
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n_map = collections.Counter(nums)
        if target in nums:
            f_ind = nums.index(target)
            l_ind = n_map[target] + f_ind - 1
            return [f_ind, l_ind]
        return [-1,-1]