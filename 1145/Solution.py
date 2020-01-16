```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        self.x_address=0
        def dfs(node):
            if not node:
                return
            if node.val==x:
                self.x_address=node
                return 
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        
        def count_node(node):
            if not node:
                return 0
            return 1+count_node(node.left)+count_node(node.right)
        
        x_node_count=count_node(self.x_address)
        total=count_node(root)
        x_left_count=count_node(self.x_address.left)
        x_right_count=count_node(self.x_address.right)
        if self.x_address==root:
            return x_left_count!=x_right_count
        return x_node_count<total-x_node_count or x_left_count>total-x_left_count or x_right_count>total-x_right_count
```