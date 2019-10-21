- 反中序遍历
这道题用了一个反中序遍历。我们为了让一次遍历就把树的节点转换一遍，要从大的数开始转换。因为这是二叉树，右子树的值大于根节点大于左子树，所以我们先从右子树开始遍历。
```python3
def helper(root):
            nonlocal tmp
            if not root:
                return 
            helper(root.right)
            tmp+=root.val
            root.val=tmp
            helper(root.left)
```