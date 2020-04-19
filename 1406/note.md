### 博弈论
可以采用博弈论的思想。一道题如何构成博弈论：  
1. 两个player  
2. 轮流  
3. 两个都要最优解  
定义f(i)f(i)f(i)表示在stoneValue[i:]中对方取[1,3]堆石子后可获得的最多石子数  
f(i)=sum(stoneValue[i:])−min(f(i+x))(1≤x≤3)  
也就是对于当前的player来说他所获得的石子数就是sum(stoneValue)减去另一个player获得的石子数，此时对于当前player来说希望另一个玩家获得的石子数尽量少。