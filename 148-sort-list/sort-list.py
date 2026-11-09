# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#WE SHOULD NOT USE ARRAY IN THE QUESTIONS OF LINKED LIST 
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        nums=[]
        curr=head
        while curr:
            nums.append(curr.val)
            curr=curr.next
        nums.sort()
        dummy=ListNode(0)
        prev=dummy
        curr=dummy
        for num in nums:
            curr.next=ListNode(num)
            curr=curr.next
        curr.next=None
        return prev.next
        

            

        
        