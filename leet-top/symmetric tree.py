# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # iterative soluction
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        stack = []
        stack.append(root.left)
        stack.append(root.right)

        while stack:
            p, q = stack.pop(), stack.pop()

            if p == None and q == None:
                continue

            if p == None or q == None or p.val != q.val:
                return False

            stack.append(p.left)
            stack.append(q.right)

            stack.append(p.right)
            stack.append(q.left)
        return True

    # # Recursive solution
    # def isSymmetric(self, root):
    #     if root is None:
    #         return True

    #     return self.isSymmetricRecu(root.left, root.right)

    # def isSymmetricRecu(self, left, right):
    #     if left is None and right is None:
    #         return True
    #     if left is None or right is None or left.val != right.val:
    #         return False
    #     return self.isSymmetricRecu(left.left, right.right) and self.isSymmetricRecu(left.right, right.left)