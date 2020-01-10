### 后序遍历+Recursion
这道题是后序遍历，我们要先对左右子树进行操作然后对根节点操作。  
- 根节点为空 return None  
- root.left=helper(root.left)  
- root.right=helper(root.right)  
- if root.val不在删除的list里，return root  
- 如果root要删除，if root.left:res.append(root.left), if root.right: res.append(root.right)。  否则return None