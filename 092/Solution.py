```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return head
        
        dummy=ListNode(0)
        dummy.next=head
        pre=dummy
        i=1
        
        while pre.next and i<m:
            i+=1
            pre=pre.next
            
        tail=pre
        cur=pre.next
        
        while cur.next and i<n:
            i+=1
            tmp=cur.next
            cur.next=tmp.next
            tmp.next=tail.next
            tail.next=tmp
            
        
        return dummy.next
```
