```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root:
            return -1
        
        result=[]
        
        def get_value(root,result):
            if not root:
                return
            
            else:
                result.append(root.val)
                get_value(root.left,result)
                get_value(root.right,result)
                
        get_value(root,result)
        nodes=set(result)
        if len(nodes)<=1:
            return -1
        else:
            return sorted(list(nodes))[1]
        
        # def find_second(nodes):
        #     diff_nodes = set(nodes)
        #     if len(diff_nodes) <=1:
        #         return -1
        #     else:
        #         return sorted(list(diff_nodes))[1]
        
        #return find_second(result)
```