- 自己写出来了一题 开心
自己写出来了一题，好开心。这道题的思路其实也很简单，设一个哨兵节点和cur。如果开始的时候cur=dummy。如果cur的下一个值等于val，那我们就把它下一个的值删掉，cur.next=cur.next.next。如果不等于的话，cur=cur.next。利用cur来遍历linked list。
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        dummy=ListNode(0)
        dummy.next=head
        cur=dummy
        
        while cur.next:
            if cur.next.val==val:
                cur.next=cur.next.next
            else:
                cur=cur.next
        return dummy.next
```
