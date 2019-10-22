```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res=[]
        stack=[]
        last_visit=None
        if not root:
            return res
        while stack or root:
            while root:
                stack.append(root)
                root=root.left
            
            cur_node=stack[-1]
            if not cur_node.right or cur_node.right==last_visit:
                item=stack.pop()
                res.append(item.val)
                last_visit=item
            
            elif cur_node.right:
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
    def postorderTraversal(self, root: TreeNode) -> List[int]:  
        if not root:
            return
        
        def helper(root,res):
            if not root:
                return
            helper(root.left,res)
            helper(root.right,res)
            res.append(root.val)
            return res
        
        return helper(root,[])
```