### 逆时针输出一棵树的边界值
对于一个node来说，如果这个node在整棵树的左边，对于它的root来说，如果node是root.left，那么就可以输出这个node, 如果这个node是root.right,则需保证，root没有左子树或者这个node没有左右子树，否则不输出。  
如果node在整棵树的右边，对于它的root来说，如果node是root.left,则需保证root没有right,否则不输出。如果是root.right,则可以输出node。