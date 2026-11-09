# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        odd=ListNode(0)
        even=ListNode(0)
        o=odd
        e=even
        curr=head
        pos=1
        while curr:
            if pos%2==1:
                o.next=curr
                o=o.next
            else:
                e.next=curr
                e=e.next
            curr=curr.next
            pos+=1
        e.next=None
        o.next=even.next
        return odd.next

        