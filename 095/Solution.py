```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n==0:
            return []
        
        def generate_tree(left,right):
            res=[]
            if left>right:
                return [None]
            for i in range(left,right+1):
                left_nodes=generate_tree(left,i-1)
                right_nodes=generate_tree(i+1,right)
                
                for left_node in left_nodes:
                    for right_node in right_nodes:
                        root=TreeNode(i)
                        root.left=left_node
                        root.right=right_node
                        res.append(root)
            return res
        
        return generate_tree(1,n)
```