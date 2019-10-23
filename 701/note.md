- 在二叉树中插入节点。
1. 如果根节点的左子树不存在且插入节点的值小于根节点，则插入这个节点。  
2. 如果根节点的右子树不存在且插入节点的值大于根节点，则插入这个节点。  
3. 如果左子树存在且插入节点的值小于根节点，则递归左子树和要插入的节点。  
4. 如果右子树存在且插入节点的值大于根节点，则递归右子树和要插入的节点。  
```python3
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return
        
        def helper(root,val):
            if not root:
                return
            
            if not root.left and val<root.val:
                root.left=TreeNode(val)
                return
            if not root.right and val>root.val:
                root.right=TreeNode(val)
                return
            
            if val<root.val:
                helper(root.left,val)
            else :
                helper(root.right,val)
                
            return root
        
        helper(root,val)
        return root
```