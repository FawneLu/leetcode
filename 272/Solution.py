```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def closestKValues1(self, root: TreeNode, target: float, k: int) -> List[int]:
        stack=[]
        res=[]
        while root or stack:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            if len(res)<k:
                res.append(root.val)
            else:
                if abs(float(root.val)-target)<abs(float(res[0])-target):
                    res.pop(0)
                    res.append(root.val)
            root=root.right
        
        return res
```