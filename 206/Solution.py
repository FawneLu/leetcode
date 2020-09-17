```python 3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        tmp = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return tmp

        
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy=ListNode(0)
        dummy.next=head
        
        tail=dummy
        
        while head.next:
            tmp=head.next
            head.next=tmp.next
            tmp.next=tail.next
            tail.next=tmp
        return dummy.next
```
```python 3
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        
        tail=head
        curr=head.next
        while curr:
            head.next=curr.next
            curr.next=tail
            tail=curr
            curr=head.next
        return tail
```
