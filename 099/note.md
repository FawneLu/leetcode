### 纠正一个二叉树
二叉树的特性是，中序遍历是有序的。我们要用到中序遍历。  
self.pre用于在中序遍历树的过程中，指向当前节点的前驱节点。  
解题思路是:  
1. 调用相应的函数，找出错误节点  
2. 交换两个错误节点的值