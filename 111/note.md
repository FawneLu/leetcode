- 这道题注意和最长路径区分
root不存在返回0。  
左子树存在，右子树不存在，返回左子树的最短路径。self.minDepth(root.left)+1  
左子树不存在，右子树存在，返回右子树的最短路径。return self.minDepth(root.right)+1  
左右子树都存在，返回两个中小的那一个路径。return min(self.minDepth(root.right),self.minDepth(root.left))+1
