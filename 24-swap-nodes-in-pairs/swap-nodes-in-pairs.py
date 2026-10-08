# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self,head:ListNode|None)->ListNode|None:
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy #prev is the node before the first node which we need to swap with the next one 
        while prev.next and prev.next.next:  #aage do node honi chaiye 
            first=prev.next   #previous ka agla node first node hoga 
            second=first.next # second =first .next or previous.next.next
            first.next=second.next #first ko second ke next node se connect kar diya
            second.next=first # swap occured
            prev.next=second # swap occured
            prev=first  # previous ko aage shift kr diye 
        return dummy.next


# Dummy is kept fixed as a stable starting point. prev is the moving pointer that takes the "before the current pair" position.