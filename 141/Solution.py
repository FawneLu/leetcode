```python3
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow,quick=head,head
        
        while quick and slow and quick.next:
            quick=quick.next.next
            slow=slow.next
            if slow==quick:
                return True
        return False
```
