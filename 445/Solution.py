```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1=[]
        s2=[]
        while l1:
            s1.append(l1.val)
            l1=l1.next
        while l2:
            s2.append(l2.val)
            l2=l2.next
        
        
        dummy=ListNode(0)
        carry=0
        
        while s1 or s2 or carry:
            if s1:
                carry+=s1.pop()
            if s2:
                carry+=s2.pop()
            
            dummy.val=carry%10
            cur=ListNode(carry//10)
            carry//=10
            cur.next=dummy
            dummy=cur
        
        return dummy.next if dummy.val==0 else dummy
```

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def getlen(l):
            length=0
            while l:
                length+=1
                l=l.next
            return length
        n1=getlen(l1)
        n2=getlen(l2)
        
        dummy=ListNode(0)
        if n1>n2:
            dummy.next=self.helper(l1,l2,n1-n2)
        else:
            dummy.next=self.helper(l2,l1,n2-n1)
        
        if dummy.next.val//10:
            dummy.next.val%=10
            dummy.val+=1
            return dummy
        
        return dummy.next
        
    def helper(self,l1,l2,diff):
        if not l1:
            return None
        if diff==0:
            res=ListNode(l1.val+l2.val)
        else:
            res=ListNode(l1.val)
        
        if diff==0:
            carry=self.helper(l1.next,l2.next,0)
        else:
            carry=self.helper(l1.next,l2,diff-1)
        
        if carry and carry.val//10:
            carry.val%=10
            res.val+=1
        
        res.next=carry
        return res
```