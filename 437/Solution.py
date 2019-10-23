```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        
        return self.helper(root,sum)+self.pathSum(root.left,sum)+self.pathSum(root.right,sum)
        
    def helper(self,root,sum_):
        res=0
        if not root:
            return 0
            
        sum_-=root.val
        if sum_==0:
            res+=1
        res+=self.helper(root.left,sum_)
        res+=self.helper(root.right,sum_)

        return res
```