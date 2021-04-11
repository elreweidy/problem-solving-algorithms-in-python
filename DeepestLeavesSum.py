# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        curr = [root]
        while curr:
            prev, curr = curr, [child for p in curr for child in [p.left, p.right] if child]
        return sum(node.val for node in prev)
