### 神奇
用普通的前缀和时间复杂度太高了，会超时。  
- dp  
定义函数f(i,j)f(i,j)f(i,j)表示右下角坐标为(i,j)的最大正方形边长，那么  

f(i,j)=min(f(i−1,j),f(i,j−1),f(i−1,j−1))+1  
其实可以相成，如果以i，j为右下角的正方形，如果包含的有一个数为0，则只有一个正方形，就是这个数本身。否则就看最小的正方形的个数加1。
  