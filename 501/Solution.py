# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        res=[]
        
        self.count = collections.Counter()
        self.inorder(root)
        freq = max(self.count.values())
        for i,c in self.count.items():
            if c == freq:
                res.append(i)
        return res
    
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.count[root.val] += 1
        self.inorder(root.right)