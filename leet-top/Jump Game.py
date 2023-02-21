class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        cur_inx = 0 
        max_inx = 0
        while cur_inx < len(nums):
            if cur_inx > max_inx:
                return False
            max_inx = max(max_inx, cur_inx + nums[cur_inx])
            cur_inx += 1
        return True