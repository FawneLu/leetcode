```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack=[]
        res=[]
        if not root:
            return res
        
        while stack or root:
            while root:
                res.append(root.val)
                stack.append(root)
                root=root.left
            
            cur_node=stack.pop()
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
    def preorderTraversal(self, root: TreeNode) -> List[int]:        
        if not root:
            return
        def helper(root,res):
            if not root:
                return
            res.append(root.val)
            helper(root.left,res)
            helper(root.right,res)
            return res
        
        return helper(root,[])
```