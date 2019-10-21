- 树真的好难啊，我又枯了
这个题分解成两个问题。一个是判断两个树是不是相等，第二个是判断一个数是否是另一个树的子树。判断一棵树是否是另一颗树的子树，也可以转化为一棵树的子树是否跟另一棵树相等。  
1. 判断两棵树是否相等可以用深度优先遍历。  
```python3
def DFS(self,s,t):
            if not s and not t:
                return True
            elif not s or not t:
                return False
            
            return s.val==t.val and self.DFS(s.left,t.left) and self.DFS(s.right,t.right)
```
2. 判断一个树是否是另一个树的子树  
```python3
def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        
        return self.DFS(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
```