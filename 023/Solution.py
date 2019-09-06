```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:  
        if not lists:
            return None
        
        nodes=[]
        for head in lists:
            while head:
                nodes.append(head)
                head=head.next
                
        nodes.sort(key = lambda x:x.val)
        
        for i in range(len(nodes)-1):
            nodes[i].next=nodes[i+1]
        
        if nodes:
            return nodes[0]
```
```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        res=lists[0]
        for l in lists[1:]:
            res=self.merge2lists(res,l)
        
        return res
    
    def merge2lists(self,l1,l2):
        dummy=cur=ListNode(0)
        while l1 and l2:
            if l1.val<l2.val:
                cur.next=l1
                l1=l1.next
            else:
                cur.next=l2
                l2=l2.next
            
            cur=cur.next
        
        cur.next=l1 or l2
        
        return dummy.next
```
