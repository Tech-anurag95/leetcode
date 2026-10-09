# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        nums=set(nums)
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        if curr==None:
            return None
        while curr:
           if curr.val in nums:
            prev.next=curr.next
           else:
            prev=curr
           curr=curr.next
        return dummy.next


        