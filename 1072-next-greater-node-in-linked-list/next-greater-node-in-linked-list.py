# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self,head:ListNode|None)->list[int]:
        a=[]
        curr=head
        while curr:
            a.append(curr.val)
            curr=curr.next   #array bna diye linked list se 
        ans=[0]*len(a)
        stack=[]
        for i in range(len(a)):
            while stack and a[i]>a[stack[-1]]:  #if the stack is not none and current element is greater than the top of the stack which will be the next largest element
                ans[stack.pop()]=a[i]
            stack.append(i)
        return ans
        

        