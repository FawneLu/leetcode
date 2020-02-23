```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def splitBST(self, root: TreeNode, V: int) -> List[TreeNode]:
        if not root:
            return [None,None]
        
        if root.val<=V:
            left,right=self.splitBST(root.right,V)
            root.right=left 
            return [root,right]
        
        left,right=self.splitBST(root.left,V)
        root.left=right
        return [left,root]
```