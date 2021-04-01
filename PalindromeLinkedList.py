# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        ll_unpacked = []

        while head.next != None:
            ll_unpacked.append(head.val)
            head = head.next
        ll_unpacked.append(head.val)
        rev_ll_unpacked = []
        for i in reversed(ll_unpacked):
            rev_ll_unpacked.append(i)
        if rev_ll_unpacked == ll_unpacked:
            return True
        else:
            return False