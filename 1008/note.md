- 根据前序遍历的list构建树
这道题的思路是一层层添加节点。
1. 首先确定root是preorder list的第一位。由于树的顺序跟list的顺序相同，所以我们可以将list反转然后一位一位pop。  
2. 之后的每一个item都从root开始与之进行比较。如果item小于root且root的左子树为空，则添加为root的左子树，若root的左节点存在，则再递归调用helper函数对root.left与item进行操作。如果item大于root且root的右子树为空，则添加为root的右子树。若root的右节点存在则递归调用helper对root.right和item进行操作。  
3. 主循环我们可以写成：  
```python3
 while preorder:
            item=preorder.pop()
            helper(root,item)
```
helper函数：
```python3
def helper(root,item):
            if not root:
                return
            
            if not root.left and root.val>item:
                root.left=TreeNode(item)
            if not root.right and root.val<item:
                root.right=TreeNode(item)
                
            if root.val>item:
                helper(root.left,item)
            else:
                helper(root.right,item)
```