## 注意性质，这是一棵二叉搜索树
1. Start traversing the tree from the root node.  
2. If both the nodes p and q are in the right subtree, then continue the search with right subtree starting step 1.  
3. If both the nodes p and q are in the left subtree, then continue the search with left subtree starting step 1.  
4. If both step 2 and step 3 are not true, this means we have found the node which is common to node p's and q's subtrees. and hence we return this common node as the LCA.