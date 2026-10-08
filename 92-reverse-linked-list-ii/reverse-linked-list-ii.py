# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        a=[]
        while head:
            a.append(head.val)
            head=head.next
        a=a[:left-1]+a[left-1:right][::-1]+a[right:]
        if len(a)==0:
            return None
        head=ListNode(a[0])
        curr=head
        for i in range(1,len(a)):
            curr.next=ListNode(a[i])
            curr=curr.next
        return head
        