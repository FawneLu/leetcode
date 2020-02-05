```python
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isvalid(s):
            count=0
            for c in s:
                if c=='(':
                    count+=1
                if c==')':
                    count-=1
                
                if count<0:
                    return False
            
            
            return count==0
        
        def dfs(s,start,l,r):
            if l==0 and r==0 and isvalid(s):
                res.append(s)
                return 
            
            for i in range(start,len(s)):
                if i!=start and s[i-1]==s[i]:
                    continue
    
                if s[i]=='(' or s[i]==')':
                    if r>0 and s[i]==')':
                        dfs(s[:i]+s[i+1:],i,l,r-1)
                    if l>0 and s[i]=='(':
                        dfs(s[:i]+s[i+1:],i,l-1,r)  
                        
        res=[]
        
        l,r=0,0
        for c in s:
            if c=='(':
                l+=1
            if l == 0:
                r+=(c==')')
            else:
                l-=(c==')')
        
        dfs(s,0,l,r)
        
        return res
```