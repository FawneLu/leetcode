- 最后一个树了，开心
1. left是左子树prune以后的结果，right是右子树prune之后的结果。  
2. 如果left存在且left.left，left.right不存在，且left的值为0，则把left为空。  
3. 如果right存在且right.left，right.right不存在，且right的值为0，则把right为空。  
4. root.left=left; root.right=right
```python3
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        
        left=self.pruneTree(root.left)
        right=self.pruneTree(root.right)
        
        if left and (not left.left) and (not left.right) and (left.val==0):
            left=None
        if right and (not right.left) and (not right.right) and (right.val==0):
            right=None
        
        root.left=left
        root.right=right
        
        return root
```