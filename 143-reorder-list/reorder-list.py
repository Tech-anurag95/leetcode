
class Solution:
    def reorderList(self,head:ListNode|None)->None:
        if not head:
            return
        nodes=deque()
        curr=head
        while curr:
            nodes.append(curr)
            curr=curr.next
        curr=nodes.popleft()
        while nodes:
            curr.next=nodes.pop()
            curr=curr.next
            if nodes:
                curr.next=nodes.popleft()
                curr=curr.next
        curr.next=None