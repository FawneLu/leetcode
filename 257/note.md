### Binary Tree的路径
- divide& merge  
先得到左子树和右子树的结果，然后把里面的结果加在root后面。  
```python
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

- 树好难啊我枯了
这道题先用一个DFS遍历树直到叶子节点。叶子节点只添加值，其余还要添加“->”。注意format的使用。
```python3
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
