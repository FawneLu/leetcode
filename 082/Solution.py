```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        if not head:
            return head
        
        dummy=ListNode(0)
        tail=dummy
        
        cur=head
        
        while cur and cur.next:
            
            if cur.val==cur.next.val:
                value=cur.val
                while cur and cur.val==value:
                    cur=cur.next   
                    
            else:
                tail.next=cur
                cur=cur.next
                tail=tail.next
            
        if cur:
            tail.next=cur
        else:
            tail.next=None
                        
        return dummy.next
```
