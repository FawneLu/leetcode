```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count=collections.Counter(t)
        left=0
        cnt=0
        res=""
        minlen=float('inf')
        
        for i,c in enumerate(s):
            count[c]-=1
            if count[c]>=0:
                cnt+=1
                
            while cnt==len(t):
                if minlen>i-left+1:
                    minlen=i-left+1
                    res=s[left:i+1]
                count[s[left]]+=1
                if count[s[left]]>0:
                    cnt-=1
                left+=1
        
        return res
```