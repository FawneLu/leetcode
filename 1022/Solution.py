```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        number=[]
        
        
        def helper(root,num):
            nonlocal number
            if not root:
                return
            
            if not root.left and not root.right:
                number.append(num+str(root.val))
                return
            
            helper(root.left,num+str(root.val))
            helper(root.right,num+str(root.val))
            
            return number
        
        binary_list=helper(root,"")
        #print(binary_list)
        res=0
        
        if not binary_list:
            return root.val
        
        for i in binary_list:
            res+=int(i,2)
        return res
```