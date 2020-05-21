# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,start,end):
        if not start:
            return None
        dummy=ListNode(0)
        dummy.next=start
        while dummy.next!=end:
            tmp=start.next
            start.next=tmp.next
            tmp.next=dummy.next
            dummy.next=tmp
        return [end,start]
            
        
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy=ListNode(0)
        dummy.next=head
        start=dummy
        while start.next:
            end=start
            for i in range(k-1):
                end=end.next
                if end.next==None:
                    return dummy.next
            
            res=self.reverse(start.next,end.next)
            start.next=res[0]
            start=res[1]
        return dummy.next