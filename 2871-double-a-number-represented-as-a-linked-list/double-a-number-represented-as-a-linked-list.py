# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head   #reverse the linked list 
        prev=None
        while curr:
            agla=curr.next
            curr.next=prev
            prev=curr
            curr=agla
        head=prev
        curr=head
        carry=0
        while curr:
            new=curr.val*2+carry
            curr.val=new%10
            carry=new//10
            last=curr
            curr=curr.next
        if carry:
            last.next=ListNode(carry)
        curr=head    #again reverse the linked list
        prev=None
        while curr:
            agla=curr.next
            curr.next=prev
            prev=curr
            curr=agla
        return prev
        




