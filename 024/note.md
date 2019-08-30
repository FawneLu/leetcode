- Linked List真的好难，我要枯了
这题是交换linked list里的相邻两位。同样，我们可以设置哨兵节点。在用一个cur pointer 来遍历linked list。需要注意的是，cur.next的变化，这也是在所有链表题里需要注意的地方。
```python 3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        dummy=ListNode(0)
        dummy.next=head
        cur=dummy
        
        while cur.next :
            tmp=cur.next
            if not tmp.next:
                break
            cur.next=cur.next.next
            tmp.next=cur.next.next
            cur.next.next=tmp
            
            cur=cur.next.next
            
            
            
        return dummy.next
```
