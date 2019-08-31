```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        cur_a=headA
        cur_b=headB
        count_a=0
        count_b=0
        start=None
        
        if not (headA and headB):
            return None
            
            
        while cur_a:
            count_a+=1
            cur_a=cur_a.next
        while cur_b:
            count_b+=1
            cur_b=cur_b.next
        
        cur_a=headA
        cur_b=headB
        
        if count_a>count_b:
            diff=count_a-count_b
            while diff:
                cur_a=cur_a.next
                diff-=1
        else:
            diff=count_b-count_a
            while diff:
                cur_b=cur_b.next
                diff-=1
                    
        while cur_a and cur_b:
            if cur_a is not cur_b:
                start=None
            else:
                if not start:
                    start=cur_a
            
            cur_a=cur_a.next
            cur_b=cur_b.next
        
        return start
```
