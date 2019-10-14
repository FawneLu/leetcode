- trim a tree
这道题我们要注意这是一个binary tree。每个节点左子树的所有节点的值小于该节点，每个节点右边子树的值大于该节点。  
如果root的值小于L，则把包括root在内所有的左子树置为空，对root的右子树进行递归。  
```python3
if root.val<L:
            root=self.trimBST(root.right,L,R)
```  
如果root的值大于R，则把包括root在内的所有右子树置为空，对root的左子树进行递归。  
```python3
elif root.val>R:
            root=self.trimBST(root.left,L,R)
```  
如果root的值在L和R之间，则对root的左子树和右子树分别进行递归。
```python3
else:
            root.left=self.trimBST(root.left,L,R)
            root.right=self.trimBST(root.right,L,R)
```