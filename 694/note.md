### DFS
这道题很神奇，要看有几个不同的岛。  
比起计算个数，我们需要一个list用来装岛的每个1的相对同一个岛的上一个1的位置。  
如果grid[i][j]!=1， 那就把pos置为空，重新开始。  
最后把pos转化为元组放入shape里， 返回shape的长度即可。  