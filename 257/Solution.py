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
```python3
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths=[]
        if not root:
            return paths
        
        if not root.left and not root.right:
            paths.append(str(root.val))
        
        leftpaths=self.binaryTreePaths(root.left)
        rightpaths=self.binaryTreePaths(root.right)
        
        for left_p in leftpaths:
            paths.append(str(root.val)+"->"+str(left_p))
        for right_p in rightpaths:
            paths.append(str(root.val)+"->"+str(right_p))
        
        return paths
```