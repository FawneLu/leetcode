# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def dfs(root, string):
            if not root:
                string += ""
            
            else:
                string += str(root.val) + ","
                string = dfs(root.left, string)
                string = dfs(root.right, string)
            return string
        return dfs(root, "")
    

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        def helper(lower = float("-inf"), upper = float("inf")):
            if not data or data[0] < lower or data[0] > upper:
                return None
            
            root_val = data.pop(0)
            root = TreeNode(root_val)
            root.left = helper(lower, root_val)
            root.right = helper(root_val, upper)
            return root
        
        data = [int(x) for x in data.split(",") if x]
        return helper()
    
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))