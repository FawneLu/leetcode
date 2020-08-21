# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.deepestDeep, self.res = 0, 0
        
        def dfs(node, layer):
            if not node.left and not node.right:
                if layer > self.deepestDeep:
                    self.deepestDeep = layer
                    self.res = node.val
                    return self.res
                elif layer == self.deepestDeep:
                    self.res += node.val
                    return self.res
            
            if node.left:
                dfs(node.left, layer + 1)
            if node.right:
                dfs(node.right, layer +1 )
        
        dfs(root, 0)
        return self.res
        
        
                
    
    def deepestLeavesSum2(self, root: TreeNode) -> int:
        deep_depth, res = 0, 0
        stack = [(root, 0 )]
        
        while stack:
            cur_node, cur_depth = stack.pop()
            
            if not cur_node.left and not cur_node.right:
                if cur_depth > deep_depth:
                    deep_depth = cur_depth
                    res = cur_node.val
                elif cur_depth == deep_depth:
                    res += cur_node.val
            
            else:
                if cur_node.left:
                    stack.append((cur_node.left, cur_depth + 1))
                if cur_node.right:
                    stack.append((cur_node.right, cur_depth + 1))
        
        return res
                
    
    
    def deepestLeavesSum1(self, root: TreeNode) -> int:
        if not root:
            return None
        
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            count = len(queue)
            res = 0
            for i in range (count):
                node = queue.popleft()
                res += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return res