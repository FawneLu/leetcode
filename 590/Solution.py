"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.res=[]
        
        def helper(root):
            if not root:
                return 
            for child in root.children:
                helper(child)
            self.res.append(root.val)
        
        helper(root)
        return self.res
        
    def postorder1(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack, res = [], []
        stack.append(root)
        
        while stack:
            node = stack.pop()
            for child in node.children:
                stack.append(child)
            res.append(node.val)
        
        
        return res[::-1]