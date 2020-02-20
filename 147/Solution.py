```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        dummy=ListNode(0)
        dummy.next=head
        cur=head
        
        while cur and cur.next:
            if cur.next.val<=cur.val:
                tmp=cur.next
                cur.next=tmp.next
                pre=dummy.next
                tail=dummy
                while pre:
                    if pre.val<tmp.val:
                        pre=pre.next
                        tail=tail.next
                    else:
                        tmp.next=pre
                        tail.next=tmp
                        break
            else:
                cur=cur.next
        
        return dummy.next
```