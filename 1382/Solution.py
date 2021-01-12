# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        return self.buildTree(self.dfs(root))
    
    def dfs(self,root):
        if not root:
            return []
        return self.dfs(root.left) + [root.val] + self.dfs(root.right)
    
    def buildTree(self, arr):
        if not arr:
            return None
        
        mid = len(arr)//2
        node = TreeNode(arr[mid])
        
        left = arr[:mid]
        right = arr[mid+1:]
        
        node.left = self.buildTree(left)
        node.right = self.buildTree(right)
        
        return node