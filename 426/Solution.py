```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        head,tail=self.helper(root)
        return head
        
    def helper(self,root):
        head, tail = root, root
        if root.left:
            left_head,left_tail=self.helper(root.left)
            left_tail.right=root
            root.left=left_tail
            head=left_head
        if root.right:
            right_head,right_tail=self.helper(root.right)
            right_head.left=root
            root.right=right_head
            tail=right_tail
        
        head.left = tail
        tail.right = head
        return head, tail
```