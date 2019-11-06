##这道题是郭老师给我讲的，就是删除二叉搜索树中的节点
首先我们要学会删除二叉搜索树的思路  
1. 首先我们要确定二叉搜索树就是左子树的所有值小于根节点，右子树的所有值大于根节点。如果要删除的值小于根节点的值，我们就递归左子树，如果要删除的值大于根节点的值我们就递归右子树。如果根节点的值等于要删除的值，那么我们继续思考接下去的问题。  
2. 如果要删除的节点左子树不存在，我们只要返回右子树；如果要删除的节点右子树不存在，我们只要返回左子树。如果两个子树都存在我们有两种处理方式。  
- 我们可以直接把要删除的节点值变更为的右子树的最小值，然后再对右子树进行递归  
```python3
if root.left and root.right:
                p=root.right
                while p.left:
                    p=p.left
                root.val=p.val
```  
- 用右子树的最小值替换要删除的节点，并将右子树的最小值指向要删除的节点的左子树。这里要注意，我们return right，直接返回右子树，相当于把左子树接在右子树的最小值上。  
```python3
if root.left and root.right:
                left=root.left
                right=root.right
                p=right
                while p.left:
                    p=p.left
                p.left=left
                return right
```