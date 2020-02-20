```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        def getlen(l):
            n=0
            while l:
                n+=1
                l=l.next
            return n
        
        n=getlen(head)
        
        res=0
        cur=head
        while cur:
            n-=1
            if cur.val:
                res+=2**n
            cur=cur.next
        
        return res
```