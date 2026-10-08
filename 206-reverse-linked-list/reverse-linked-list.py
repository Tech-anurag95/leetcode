# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self,head:ListNode|None)->ListNode|None:
        a=[]
        while head:
            a.append(head.val)
            head=head.next
        a=a[::-1]  #linkedlist se array bna diya 
        if not a:   #agar array ki length 0 hai to return None
            return None
        head=ListNode(a[0])   #phle element ko head bna diya 
        curr=head  #ye ek pointer variable hai 
        for i in range(1,len(a)):
            curr.next=ListNode(a[i])
            curr=curr.next
        return head



        