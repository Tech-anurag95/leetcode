# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: ListNode | None, k: int) -> list[ListNode | None]:
        length=0
        curr=head
        while curr:
            length+=1
            curr=curr.next
        size=length//k
        extra=length%k
        curr=0
        ans=[]
        current=head
        while curr<extra:
            elements=0
            abhi=current
            while elements<size+1:
                prev=current
                current=current.next
                elements+=1
            prev.next=None
            ans.append(abhi)
            curr+=1
        curr=0
        while curr<k-extra:
            elements=0
            abhi=current
            while elements<size:
                prev=current
                current=current.next
                elements+=1
            if elements>0:
                prev.next=None
            ans.append(abhi)
            curr+=1
        return ans
        
            



        