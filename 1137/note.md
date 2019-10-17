- 参考斐波那契数列
题目已经给出边界条件。n==0,返回0。n==1，返回1，n==2也返回1。  
res=helper(n-1)+helper(n-2)+helper(n-3)