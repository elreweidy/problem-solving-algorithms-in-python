# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original:
            return None
        stack = collections.deque([(original, cloned)])

        while stack:
            og, clone = stack.popleft()
            if og == target:
                return clone
            if og.right:
                stack.append((og.right, clone.right))
            if og.left:
                stack.append((og.left, clone.left))
        return None




