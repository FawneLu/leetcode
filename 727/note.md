### 动态规划
这道题的思路非常奇妙。用一个cur来存储一个连续的string。  
cur[i]对应的是string开始的index，i对应的是string结束的index。  
最后用一个ans找出它最短的第一个string。