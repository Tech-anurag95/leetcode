# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self,head:ListNode|None)->ListNode|None:
        curr=head
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        temp=curr.next
        while curr:
            if curr.val==0:
                prev.next=curr.next
                curr=curr.next
                if curr:
                    temp=curr.next
            else:
                if temp.val!=0:
                    curr.val+=temp.val
                    curr.next=temp.next
                    temp=temp.next
                else:
                    prev=curr
                    curr=temp
        return dummy.next

            



        