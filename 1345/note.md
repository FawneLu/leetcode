### BFS
初始是在下标为0的点，每一次跳跃可以跳到左侧，右侧或者任意值跟当前值相同的下标处，最终目标是到达最后一个下标。  

过程就是标准的BFS，但此题很容易超时，需要做额外处理：  

如果有一段连续的区间上所有元素的值相等，那么只需保留左右端点。
比如对于一个输入比如：  

[7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 9]来说，如果我们从第一个7开始跳，实际上直接一步跳到最远的7即可，中间的所有7都是无效的。  
