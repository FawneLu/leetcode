```python3
class Solution:
    def reverseWords(self, s: str) -> str:
        s_list=s.split()
        res=""
        if len(s_list)==0:
            return ""
        
        for i in s_list:
            i=i[::-1]
            res=res+i
            res=res+" "
        
        
        return res[:-1]
```
