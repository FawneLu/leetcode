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
```python3
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
