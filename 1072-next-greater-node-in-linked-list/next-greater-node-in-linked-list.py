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
            curr=curr.next
        ans=[0]*len(a)
        stack=[]
        for i in range(len(a)):
            while stack:
                if a[i]>a[stack[-1]]:
                    index=stack.pop()
                    ans[index]=a[i]
                else:
                    break
            stack.append(i)
        return ans
        

        