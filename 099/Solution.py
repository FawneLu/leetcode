```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.pre=None
        self.mistake_1=None
        self.mistake_2=None
        
        self.inOrder(root)
        self.mistake_1.val, self.mistake_2.val = self.mistake_2.val, self.mistake_1.val
        
     
    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        if self.pre and self.pre.val>root.val:
            if not self.mistake_1:
                self.mistake_1=self.pre
            self.mistake_2=root
        self.pre=root
        self.inOrder(root.right)
```