- Most Common Way (Master Zhang said this is the most correct way of thinking, hhhhh I'm fucking genius!) 
We need two variables. One is to record the previous minium value before the judging position. One is to record the currect minium money. (一个用来记录运行到当前位置的之前最小值，一个用来记录运行到当前位置的交易的最大值)  
```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        money=0
        if len(prices)<=1:
            return 0
        pre_min=prices[0]
        for i in range(0,len(prices)-1):
            if prices[i+1]<pre_min:
                pre_min=prices[i+1]
                continue
            if prices[i+1]-pre_min>money:
                money=prices[i+1]-pre_min
        return money
```  
