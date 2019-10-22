- 利用中序遍历和后序遍历构造一棵树
根据后序遍历的特征，list的最后一个数是根节点。  
1. 找到后序遍历list的最后一个数在inorderlist中对应的位置。  
2. 这个结点把inorder list划分为左右两棵子树。左边为左子树，右边为右子树。  
3. 先对右子树进行递归，因为postorder pop出来的是右子树的根节点。  
4. 再对左子树进行递归。
```python3
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return
        index=inorder.index(postorder.pop())
        root=TreeNode(inorder[index])
        root.right=self.buildTree(inorder[index+1:],postorder)
        root.left=self.buildTree(inorder[:index],postorder)
        
        return root
```