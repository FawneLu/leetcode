```python
class Solution:
    def countAndSay(self, n: int) -> str:
        res='1'
        for i in range(n-1):
            new_res,pre,count='',res[0],0
            for j in range(len(res)):
                if res[j]==pre:
                    count+=1
                else:
                    new_res+=str(count)+pre
                    count=1
                    pre=res[j]
            res=new_res+str(count)+pre
        return res
```