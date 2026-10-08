# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        a=[]
        curr=head
        while curr:
            a.append(curr.val)
            curr=curr.next
        size=len(a)  #total kitne nodes hain
        if size==0:   #agar linked list empty hui to 
            return None
        if n==size:    #last se len(a) mtlb phla element isliye hum second element se list ko return kr denge 
            return head.next
        count=0
        curr=head
        while curr:
            if count==size-n-1:   #size-n-1 = last se nth node
               curr.next=curr.next.next  
               break
            curr=curr.next #agar last se nth pe nhi hain to aage bdhenge 
            count+=1  #aur count ko 1 aage krenge 
        return head



#return mein hum jis node ka reference return karte hain, linked list wahi se start hoti hai


        