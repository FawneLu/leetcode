```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        def dfs(root,isl,isr):
            if root:
                isleaf=not root.left and not root.right
                if isl or isleaf:
                    res.append(root.val)
                dfs(root.left,isl,isr and not root.right)
                dfs(root.right,isl and not root.left, isr)
                
                if isr and not isleaf:
                    res.append(root.val)
        
        if not root:
            return []
        res=[root.val]
        dfs(root.left,True,False)
        dfs(root.right,False,True)
        return res
```