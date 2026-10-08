# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode | None) -> ListNode | None:
        a=[]
        curr=head
        while curr:
            a.append(curr.val)
            curr=curr.next
        a.sort()
        if not a:
            return None
        head=ListNode(a[0])
        curr=head
        for i in range(1,len(a)):
            curr.next=ListNode(a[i])
            curr=curr.next
        return head


        