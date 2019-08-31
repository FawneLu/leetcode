- easy?
For this question, we need to judge whether the value of current node is the same with next one. We need to use cur.val==cur.next.val to do the judgement.
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
        cur=dummy=head
        
        while cur.next:
            if cur.val==cur.next.val:
                cur.next=cur.next.next
            else:
                cur=cur.next
                
        return dummy
```
