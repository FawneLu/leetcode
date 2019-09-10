- 使用carry
The standard way is to use a pointer carry to determine whether the sum of two list need to carry. We make sum=l1.val+l2.val+carry. And the new list always point to ListNode(add%10).
Here we need to know that ListNode(add%10) means the value of this node is add%10.
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy= ListNode(0)
        cur=dummy
        carry=0
        
        while l1 and l2:
            add=l1.val+l2.val+carry
            if add>=10:
                carry=1
            else:
                carry=0
            cur.next=ListNode(add%10)
            cur=cur.next
            l1=l1.next
            l2=l2.next
            
        if l1:
            l=l1
        else:
            l=l2
        
        while l:
            add=l.val+carry
            if add>=10:
                carry=1
            else:
                carry=0
            cur.next=ListNode(add%10)
            cur=cur.next
            l=l.next
        
        if carry==1:
            cur.next=ListNode(1)
            
        return dummy.next
```
- simple way
We use two strings to store l1 and l2. We add two strings and then convert it to linked list.
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1=''
        num2=''
        
        while l1:
            num1+=str(l1.val)
            l1=l1.next
        
        while l2:
            num2+=str(l2.val)
            l2=l2.next
            
        print(num1,num2)
        
        add=str(int(num1[::-1])+int(num2[::-1]))[::-1]
        print(add)
        
        dummy=ListNode(0)
        res=dummy
        for i in range(len(add)):
            res.next=ListNode(add[i])
            res=res.next
        return dummy.next
```
