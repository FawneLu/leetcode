```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        dic=dict()
        
        def helper(root,parentused):
            if not root:
                return 0
            if (root,parentused) in dic:
                return dic[(root,parentused)]
            res=0
            if parentused:
                res=helper(root.left,False)+helper(root.right,False)
            else:
                res=max(helper(root.left,False)+helper(root.right,False),root.val+helper(root.left,True)+helper(root.right,True))
            
            dic[(root,parentused)]=res
            return res
        
        res=helper(root,False)
        
        return res
```