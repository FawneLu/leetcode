```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        left=root.left
        right=root.right
        root.left=None
        self.flatten(left)
        self.flatten(right)
        
        root.right=left
        
        while root.right:
            root=root.right
        
        root.right=right
        
    
    
    def flatten1(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res=[]
        def preorder(root):
            if not root:
                return 
            res.append(root)
            preorder(root.left)
            preorder(root.right)
        
        preorder(root)
        
        for i in range(len(res)-1):
            res[i].left=None
            res[i].right=res[i+1]
```