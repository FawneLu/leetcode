### 二分查找 最小化最大值
这道题跟之前那道切巧克力的有差别。一个是最小化最大值，一个是最大化最小值。  
- 最小化最大值：  
high=sum(list)  
low=sum(list)//m  
对于cursum来说，应该在判断cursum是否大于mid后再加。  
- 最大化最小值：  
high=sum(list)//m  
low=min(list)  
对于cursum来说，应该在判断cursum是否大于mid前再加。