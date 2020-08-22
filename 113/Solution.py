# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.res = []
        
        def helper(root, cum, path):
            if not root:
                return 0
             
            cum -= root.val
            if cum == 0 and not root.left and not root.right:
                self.res.append(path + [root.val])
                
            helper(root.left, cum, path + [root.val])
            helper(root.right, cum, path + [root.val])
            
        helper(root, sum, [])
        
        return self.res