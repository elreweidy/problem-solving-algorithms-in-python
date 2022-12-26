class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter = []
        i = 0

        while nums1 and nums2:
            if nums1[i] in nums2:
                inter.append(nums1[i])
                r = nums1[i]
                nums1.remove(r)
                nums2.remove(r)
            else:
                nums1.remove(nums1[i])

        return inter