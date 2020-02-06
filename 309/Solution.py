```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        sell=[0]*len(prices)
        hold=[0]*len(prices)
        hold[0]=-prices[0]
        for i in range(1,len(prices)):
            sell[i]=max(hold[i-1]+prices[i],sell[i-1])
            hold[i]=max(hold[i-1],(sell[i-2] if i >2 else 0)-prices[i] )
        return sell[-1]
```