- 把树转化为string输出
这是一道简单的递归求解树的问题。我们只需要考虑当前节点的情况。  
1. 如果节点不存在就返回空值。   
2. 如果不存在左右子树就把该节点转化为string输出。  
3. 如果不存在右子树就递归左子树然后输出。  
4. 除了以上的情况，就对左右子树同时进行递归。
```python3
def preorder(t):
            if not t:
                return ""
            if not t.left and not t.right:
                return str(t.val)
            elif not t.right:
                return str(t.val)+"("+preorder(t.left)+")"
            else:
                return str(t.val)+"("+preorder(t.left)+")"+"("+preorder(t.right)+")"
```