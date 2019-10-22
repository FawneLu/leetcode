```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack=[]
        res=[]
        if not root:
            return res
        
        while stack or root:
            while root:
                stack.append(root)
                root=root.left
            cur_node=stack.pop()
            res.append(cur_node.val)
            root=cur_node.right
        
        return res
```

```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        if not root:
            return 
        
        def helper(root,res):
            if not root:
                return 
            helper(root.left,res)
            res.append(root.val)
            helper(root.right,res)
            
            return res
        
        return helper(root,[])
```