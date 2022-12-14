# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # # iterative solution
        if not head: return None

        prev = None
        cur = head

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev

        # # recursion soluction
        def rec(prev, cur):
            if not cur:
                return prev
            tail = rec(cur, cur.next)
            cur.next = prev

            return tail

        return rec(None, head)