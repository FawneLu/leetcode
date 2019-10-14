```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # if not head:
        #     return head
        
        small=ListNode(0)
        large=ListNode(0)
        small_r=small
        large_r=large
        
        while head:
            if head.val<x:
                small.next=head
                small=small.next
            else:
                large.next=head
                large=large.next
                
            tmp=head.next
            head.next=None
            head=tmp
        
        small.next=large_r.next
        
        return small_r.next
```
