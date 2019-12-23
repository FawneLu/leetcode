```python
class Solution:
    def intToRoman(self, num: int) -> str:
        Thousands=["","M","MM","MMM"]
        Percentile=["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        Deciles=["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        Quantiles=["","I","II","III","IV","V","VI","VII","VIII","IX"]
        return Thousands[num//1000]+Percentile[(num%1000)//100]+Deciles[(num%100)//10]+Quantiles[(num%10)]
```