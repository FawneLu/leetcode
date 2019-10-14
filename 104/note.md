- 写过三个类似的题
这道题的思路很简单。首先我们设一个helper函数。  
root不存在就返回0  
left=helper(root.left)(left等于左子树的长度)  
right=helper(root.right)(right等于右子树的长度)  
depth=max(left,right)(depth为左子树和右子树中最长的那一个)  return depth(返回depth)
