# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode | None, nums: list[int]) -> int:
        nums=set(nums)
        count=0
        curr=head
        while curr:
            if curr.val in nums and (curr.next==None or curr.next.val not in nums):
                count+=1
            curr=curr.next
        return count

        