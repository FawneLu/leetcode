```python
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        d={}
        for transaction in transactions:
            if transaction[0] not in d:
                d[transaction[0]]=-transaction[2]
            else:
                d[transaction[0]]-=transaction[2]
            if transaction[1] not in d:
                d[transaction[1]]=transaction[2]
            else:
                d[transaction[1]]+=transaction[2]
        
        
        debt=[]
        for value in d.values():
            debt.append(value)
        
        
        def helper(debt,start,count):
            res=float('inf')
            n=len(debt)
            while start<n and debt[start]==0:
                start+=1
            
            if start==n:
                return count
            
            for i in range(start+1,n):
                if debt[start]*debt[i]<0:
                    debt[i]+=debt[start]
                    res=min(res,helper(debt,start+1,count+1))
                    debt[i]-=debt[start]
            
            return res
        
        
        return helper(debt,0,0)
```