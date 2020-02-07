```python
class Solution:
    def countBits(self, num: int) -> List[int]:
        dp=[0]*(num+1)
        for i in range(1,num+1):
            dp[i]=dp[i//2]+i%2
        return dp
       
#     def countBits(self, num: int) -> List[int]:
#         res=[]
#         for i in range(num+1):
#             count=0
#             num_b=bin(i)
#             for c in num_b:
#                 if c=='1':
#                     count+=1
#             res.append(count)
        
#         return res
```