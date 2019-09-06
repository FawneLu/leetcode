- 第一种思路
We use a list to store every value in the linked list then we reverse the list and compare the list with the linked list.
```python3
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverse(self,midpoint):
        head=tail=midpoint.next
        while head.next:
            tmp=head.next
            head.next=head.next.next
            tmp.next=tail
            tail=tmp
        midpoint.next=tail
        return midpoint
        
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        cur=head
        values=[]
        while cur:
            values.append(cur.val)
            cur=cur.next
        values.reverse()
        i=0
        for value in values:
            if value==head.val:
                head=head.next
            else:
                return False
        return True
```
- 第二种思路
We use a slow and quick pointer. Slow pointer take one step every time and quick pointer takes two steps every time. When the quick pointer reaches the end the slow pointer just reaches the mid. Then we reverse the second half of the linked list and compare it with the first half from head.
```python3
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverse(self,midpoint):
        head=tail=midpoint.next
        while head.next:
            tmp=head.next
            head.next=head.next.next
            tmp.next=tail
            tail=tmp
        midpoint.next=tail
        return midpoint
        
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if not head or not head.next:
            
            return True
        
        slow=quick=head
        while quick.next and quick.next.next:
            slow=slow.next
            quick=quick.next.next
            
        slow=self.reverse(slow)
        slow=slow.next
        
        while slow:
            if head.val==slow.val:
                head=head.next
                slow=slow.next
            else:
                return False
        return True
```
