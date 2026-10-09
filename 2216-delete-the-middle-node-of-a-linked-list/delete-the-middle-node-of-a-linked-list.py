# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self,head:ListNode|None)->ListNode|None:
        if head.next is None:
            return None
        curr=head
        size=0
        while curr:
            size+=1
            curr=curr.next
        mid=size//2
        curr=head
        i=0
        while i<mid-1:
            curr=curr.next
            i+=1
        curr.next=curr.next.next
        return head
        