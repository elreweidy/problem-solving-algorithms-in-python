# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1v, l2v = [], []
        l1_c, l2_c = l1, l2

        while l1_c:
            l1v.append(l1_c.val)
            l1_c = l1_c.next

        while l2_c:
            l2v.append(l2_c.val)
            l2_c = l2_c.next

        l1v = list(reversed(l1v))
        l2v = list(reversed(l2v))
        x, y = 0, 0
        for i in range(len(l1v)):
            x += l1v[i] * (10 ** ((len(l1v) - i) - 1))

        for i in range(len(l2v)):
            y += l2v[i] * (10 ** ((len(l2v) - i) - 1))

        ol = list(str(x + y))
        tail = None
        for i in range(len(ol)):
            tail = ListNode(int(ol[i]), tail)
            print(tail.val)

        return tail