```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res=[]
        ds=set(to_delete)
        def helper(root):
            if not root:
                return None
            
            root.left=helper(root.left)
            root.right=helper(root.right)
            
            if root.val not in ds:
                return root
            if root.left:
                res.append(root.left)
            if root.right:
                res.append(root.right)
            
            return None
            
        
        root=helper(root)
        if root:
            res.append(root)
        return res
```