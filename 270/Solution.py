```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        res=root.val
        
        if target<root.val and root.left:
            left=self.closestValue(root.left,target)
            if abs(float(res)-target)>=abs(float(left)-target):
                res=left 
        
        if target>root.val and root.right:
            right=self.closestValue(root.right,target)
            if abs(float(res)-target)>=abs(float(right)-target):
                res=right 
        return res
    
    
    
    
    
    def closestValue2(self, root: TreeNode, target: float) -> int:
        res=root.val
        while root:
            if abs(float(res)-target)>=abs(float(root.val)-target):
                res=root.val
            if root.val>target:
                root=root.left
            else:
                root=root.right
        return res
        
        
    def closestValue1(self, root: TreeNode, target: float) -> int:
        stack=[]
        diff=float('inf')
        res=0
        while root or stack:
            while root:
                stack.append(root)
                root=root.left
            
            root=stack.pop()
            if abs(float(root.val)-target)<diff:
                diff=abs(float(root.val)-target)
                res=root.val
            root=root.right
        
        return res
```