class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        dummy=ListNode(0)
        dummy.next=head
        phla=dummy
        def reverse(start):
            prev=None
            curr=start
            while curr:
                agla=curr.next
                curr.next=prev
                prev=curr
                curr=agla
            return prev
        while True:
            num=1
            start=phla.next
            curr=start
            while curr and num<k:
                curr=curr.next
                num+=1
            if not curr:
                break
            agla=curr.next
            curr.next=None
            newhead=reverse(start)
            phla.next=newhead
            start.next=agla
            phla=start
        return dummy.next
        



                 

