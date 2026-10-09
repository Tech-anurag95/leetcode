# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr=head
        a=[]
        while curr:
            a.append(curr.val)
            curr=curr.next
        a[k-1],a[len(a)-k]=a[len(a)-k],a[k-1]
        curr=head
        i=0
        while curr:
            curr.val=a[i]
            i+=1
            curr=curr.next
        return head

        