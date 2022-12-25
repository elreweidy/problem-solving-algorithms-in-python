class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(list(set(nums))) == len(nums): return False
        else: return True