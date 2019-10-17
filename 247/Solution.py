```python3
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        def helper(n,m):
            if n==0:
                return [""]
            if n==1:
                return ["0","1","8"]
            
            res=[]
            
            for num in helper(n-2,m):
                if n!=m:
                    res.append("0"+num+"0")
                res.append("1"+num+"1")
                res.append("6"+num+"9")
                res.append("8"+num+"8")
                res.append("9"+num+"6")
                
            return res
        
        return helper(n,n)
```