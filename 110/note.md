- 判断平衡二叉树
一个平衡二叉树不仅需要满足左右子树的高度差小于等于1，同时对于每个节点的左子树来说需要是一个平衡二叉树，右子树也需要是一个平衡二叉树。abs(self.depth(root.left)-self.depth(root.right))<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)  
计算树的高度可以记住：  
def depth(self,root):
        if not root:
            return 0
        return max(self.depth(root.left),self.depth(root.right))+1

