# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self,head:ListNode|None,k:int)->ListNode|None:
        if head is None or head.next is None:
            return head
        curr=head
        length=0
        while curr:
            length+=1
            curr=curr.next
        rotation=k%length
        if rotation==0:
            return head
        x=0
        while x<rotation:
            curr=head
            while curr.next.next:
                curr=curr.next
            last=curr.next   #mtlb hum second last node pe phoch gye aur last node ko last man liye
            curr.next=None  #last element ko skip krna hai 
            last.next=head #ab last wala start me jayega 
            head=last #head will point to last
            x+=1  #ROTATION COUNT KO ek bdha denge
        return head




        
        