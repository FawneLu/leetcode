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