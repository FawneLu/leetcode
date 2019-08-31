- 代码长但思路清晰
这道题的思路，还是比较清晰的。虽然我没有写出来。首先，我们先把两个linked list遍历一遍，求出每个linked list的长度，然后我们把长的那个linked list从头开始缩减到和短的那个一样长。接着，我们判断两个linked list是否相同。如果相同，在start指针为None的情况下，就把它置为相同的linked_list开始的地方，如果不同就置为空。
```python3
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
