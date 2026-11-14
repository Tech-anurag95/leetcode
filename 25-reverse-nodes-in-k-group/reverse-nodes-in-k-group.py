class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        dummy=ListNode(0)
        dummy.next=head
        phla=dummy
        def reverse(start):
            curr=start
            prev=None
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
            while num<k and curr:
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


# find the segment 
# reverse it 
# start se reversed wale ke start ko jodo
# reversed ke end ko original ke start se jodo (start.next=agla)
# restart kro (phla =start)
                 

