class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''
import math


def heightinorder(root):
    inorder = []

    if root:
        inorder = heightinorder(root.left)
        inorder.append(root)
        inorder.append(root)
        inorder = inorder + heightinorder(root.right)

    return inorder


def height(root):
    level_1 = 0
    level_2 = 0
    inorder = heightinorder(root)
    spl = 0
    for i in range(len(inorder) - 1):
        if inorder[i] == inorder[i + 1]:
            level_1 = i + 1

            spl = inorder[i]

            level_2 = len(inorder) - (i + 1)
            break
    return max(math.ceil(int(level_1 / 3)), math.ceil(int(level_2 / 3)))


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(height(tree.root))
