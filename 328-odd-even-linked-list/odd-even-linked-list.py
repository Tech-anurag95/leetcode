# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        oddlist=ListNode(0)
        evenlist=ListNode(0)
        odd=oddlist
        even=evenlist
        curr=head
        count=1
        while curr:
            if count%2==1:
                odd.next=ListNode(curr.val)
                odd=odd.next
            else:
                even.next=ListNode(curr.val)
                even=even.next
            count+=1
            curr=curr.next
        odd.next=evenlist.next
        return oddlist.next


        

        