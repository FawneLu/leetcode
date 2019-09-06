```python3
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # visited=set()
        # while head:
        #     visited.add(head)
        #     head=head.next
        #     if head in visited:
        #         return head
        # return None
        
        quick=slow=head
        while quick and slow and quick.next:
            quick=quick.next.next
            slow=slow.next
            if quick==slow:
                start=head
                while start!=quick:
                    start=start.next
                    quick=quick.next
                return start
        return None
```
