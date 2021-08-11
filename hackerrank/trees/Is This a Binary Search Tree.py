""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


def inorderTraversal(root):
    inorder = []

    if root:
        inorder = inorderTraversal(root.left)

        inorder.append(root.data)

        inorder = inorder + inorderTraversal(root.right)

    return inorder


def checkBST(root):
    tree_values = inorderTraversal(root)
    for i in range(len(tree_values) - 1):
        if tree_values[i] > tree_values[i + 1] or tree_values[i] == tree_values[i + 1]:
            return False

    return True