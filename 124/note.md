### 求二叉树的最大子树的和
需要注意两个地方：  
- 我们需要一个全局变量来实时更新当前最大子树的和  
- 递归函数返回的是max(left+root.val,right+root.val)因为，如果需要向上一层递归，则不可能同时经过同一个节点的左右子树。