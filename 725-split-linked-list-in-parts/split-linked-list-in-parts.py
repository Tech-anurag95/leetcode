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
        ans=[]
        start=0
        while start<extra:
            curr=head
            abhi=curr
            count=1
            while count<size+1:
                curr=curr.next
                count+=1
            head=curr.next
            curr.next=None
            ans.append(abhi)
            start+=1
        start=0
        while start<(k-extra):
            if size==0:
                ans.append(None)
                start+=1
                continue
            curr=head
            abhi=curr
            count=1
            while count<size:
                curr=curr.next
                count+=1

            head=curr.next
            curr.next=None
            ans.append(abhi)
            start+=1
        return ans
        
        
            
        


        
            



        