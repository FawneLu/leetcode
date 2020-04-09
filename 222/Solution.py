# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def getheight(root):
            height=0
            while root:
                height+=1
                root=root.left
            return height
        
        nodes=0
        
        left_height=getheight(root.left)
        right_height=getheight(root.right)
        
        if left_height==right_height:
            nodes+=2**left_height+self.countNodes(root.right)
        else:
            nodes+=2**right_height+self.countNodes(root.left)
            
        return nodes
    



    def countNodes2(self, root: TreeNode) -> int:
        return 1+self.countNodes(root.left)+self.countNodes(root.right) if root else 0


    def countNodes3(self, root: TreeNode) -> int:
        
        def helper(root,res):
            if not root:
                return 0
            else:
                res=res+helper(root.left,res)+helper(root.right,res)
            
            return res+1
        
        return helper(root,0)