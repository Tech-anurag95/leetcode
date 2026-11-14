# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        curr=head
        prev=head
        hello=head
        curr=head.next
        while curr:
            new=ListNode(gcd(prev.val,curr.val))
            prev.next=new
            new.next=curr
            prev=curr
            curr=curr.next
        return hello
        