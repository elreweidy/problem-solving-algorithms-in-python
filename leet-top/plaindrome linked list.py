# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head: return True

        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        if len(vals) == 1:
            return True
        if len(vals) % 2 == 0:
            mid = len(vals) // 2
            if vals[:mid+1] == list(reversed(vals[mid-1:])):
                return True
            else:
                return False
        else:
            mid = len(vals) // 2 + 1
            if vals[:mid] == list(reversed(vals[mid-1:])):
                return True
            else:
                return False