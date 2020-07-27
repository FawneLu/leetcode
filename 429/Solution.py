"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        
        def getlevel(root, level, res):
            if not root:
                return
            
            if level == len(res):
                res.append([])
            res[level].append(root.val)
            for child in root.children:
                getlevel(child, level+1, res)
        
        getlevel(root, 0, res)
        return res
        
        
        
    
    
    
    def levelOrder1(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        queue = collections.deque()
        queue.append(root)
        res=[]
        
        while queue:
            l = len(queue)
            cur_ans = []
            
            for _ in range(l):
                node = queue.popleft()
                cur_ans.append(node.val)
                
                for child in node.children:
                    queue.append(child)
                    
            res.append(cur_ans)
        
        return res