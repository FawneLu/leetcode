```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy=ListNode(0)
        dummy.next=head
        quick=slow=dummy
        while quick:
            if n>=0:
                n-=1
                quick=quick.next
            else:
                quick=quick.next
                slow=slow.next
                
        slow.next=slow.next.next
        return dummy.next
```
```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur=head
        len_node=1
        while cur.next:
            len_node+=1
            cur=cur.next
        count=len_node-n
        print(len_node)
        print(count)
        
        dummy=ListNode(0)
        dummy.next=head
        
        cur=dummy
        
        while count:
            cur=cur.next
            count-=1
        cur.next=cur.next.next
        return dummy.next
```
```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur=head
        len_node=1
        while cur.next:
            len_node+=1
            cur=cur.next
        count=len_node-n
        print(len_node)
        print(count)
        
        dummy=ListNode(0)
        dummy.next=head
        
        cur=dummy
        
        len_n=0
        while cur:
            if len_n==count:
                cur.next=cur.next.next
                break
            len_n+=1
            cur=cur.next
        return dummy.next
```
