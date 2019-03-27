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