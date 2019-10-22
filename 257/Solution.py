```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return[]
        
        return self.DFS(root,"",[])
        
        
        
    def DFS(self,root,path,paths):
        if not root:
            return 
        
        if not root.left and not root.right:
            path+="{}".format(root.val)
            paths.append(path)
        path+="{}->".format(root.val)
        
        self.DFS(root.left,path,paths)
        self.DFS(root.right,path,paths)
        
        return paths
```