```python3
class Solution:
    def romanToInt(self, s: str) -> int:
        d={}
        dic = [('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100),('D', 500),('M', 1000)]
        for i,j in dic:
            d[i]=j
        print(d)
        
        res=d[s[-1]]
        
        s=s[::-1]
        
        for i in range (len(s)-1):
            if d[s[i]]>d[s[i+1]]:
                res-=d[s[i+1]]
            else:
                res+=d[s[i+1]]
            
        return res
```