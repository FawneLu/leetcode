- 唉，树真的好难啊
这道题的思路是，如果左子树为空或者值等于根节点的值而且右子树也满足相同条件，此时为univalue subtree。我们对根节点进行递归。如果满足条件则返回根节点的值未下一次判定目标，否则返回“#”。
```python3
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        count=0
        def helper(root):
            nonlocal count
            if not root:
                return
            left=helper(root.left)
            right=helper(root.right)
            
            if (not left or left==root.val) and (not right or right==root.val):
                count+=1
                return root.val
            return "#"
        
        helper(root)
        return count
```