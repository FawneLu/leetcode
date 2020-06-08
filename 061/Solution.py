# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        count=1
        curr=head
        while curr.next:
            count+=1
            curr=curr.next
        k%=count 
        slow,fast=head,head
        if k==0:
            return head
        while k-1:
            fast=fast.next
            k-=1
        while fast.next:
            pre=slow
            slow=slow.next
            fast=fast.next
        
        pre.next=None
        fast.next=head
        
        return slow