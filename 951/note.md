### Recursion
这道题的判断条件是，如果root1 is root2, 返回True, 如果root1 为空 或者 root2 为空 或者 root1.val!= root2.val 返回 False。  
只需回溯2种情况:  
(root1.left, root2.left) and (root1.right, root2.left)   
(root1.left, root2.right) and (root1.right, root2.left)