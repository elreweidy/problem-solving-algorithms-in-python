# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        if cur.next == None:
            return cur

        node = head
        total = 1
        while head.next!=None:
            total+= 1
            head = head.next

        mid = total // 2
        total = 0
        while node:
            if total == mid:
                return node
            else:
                total+=1
                node = node.next
        return None