# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if head==None or head.next==None:
            return head
        cur = head
        temp = cur.next
        cur.next = temp.next
        temp.next = cur
        prev = cur
        head = temp
        cur = cur.next
        while cur!=None and cur.next!=None:
            temp = cur.next
            cur.next = temp.next
            temp.next = cur
            prev.next = temp
            prev = cur
            cur = cur.next
        return head
        