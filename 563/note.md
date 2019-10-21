- 简单递归，学会看return的值
这道题的思路就是一个简单的递归。我们首先看边界条件是如果不存在根节点则返回0。  
递归的时候，对一个根节点来说，返回的值应该是该节点求出了左右子树的结果后再加上该节点的值。  
同时，我们也要设一个res来保存最后的结果。
```python3
def helper(root):
            nonlocal res
            if not root:
                return 0
            
            left=helper(root.left)
            right=helper(root.right)
            
            res=res+abs(left-right)
            
            return left+right+root.val
```