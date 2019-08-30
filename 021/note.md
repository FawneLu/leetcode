- learn to insert elements in the node.
We use two pointers. One is dummy which is to record the starting place. The other is curr we use this pointer to tranverse the linked list. When l1 and l2 is not equal, we plus the surplus of the longer one to the curr.
```python3
#Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#     def __repr__(self):
#         #return "{}-> {}".format(self.val,self.next)
#         return "{}->{}".format(self.val,self.next)  

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = dummy = ListNode(0)
        while l1 and l2:
            if l1.val<l2.val:
                curr.next=l1
                l1=l1.next
            else:
                curr.next=l2
                l2=l2.next
            curr=curr.next

        curr.next=l1 or l2

        return dummy.next
```
