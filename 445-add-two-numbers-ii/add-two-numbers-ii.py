# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        def reverse(node1):
            curr=node1
            prev=None
            while curr:
                agla=curr.next
                curr.next=prev
                prev=curr
                curr=agla
            return prev
        l1=reverse(l1)
        l2=reverse(l2)
        curr1=l1
        curr2=l2
        new=ListNode(0)
        curr=new
        carry=0
        while curr1 or curr2 or carry:
            v1=curr1.val if curr1 else 0
            v2=curr2.val if curr2 else 0
            val=v1+v2+carry
            original=val%10
            carry=val//10
            curr.next=ListNode(original)
            curr=curr.next
            if curr1:
                curr1=curr1.next
            if curr2:
                curr2=curr2.next
        ans=reverse(new.next)
        return ans 
            


            


            
        