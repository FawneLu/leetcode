```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def dfs(root):
            if not root:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            
            return max(left,right)+1
        
        height=dfs(root)
        cols=2**height-1
        res=[[""]*cols for i in range(height)]
        
        def helper(node,d,pos,res):
            res[-d-1][pos]=str(node.val)
            if node.left:
                helper(node.left,d-1,pos - 2 ** (d - 1),res)
            if node.right:
                helper(node.right,d-1,pos+2**(d-1),res)
        
        helper(root,height-1,2**(height-1)-1,res)
        return res
```