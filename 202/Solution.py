```python
class Solution:
    def isHappy(self, n: int) -> bool:
        def square(num):
            return num**2
        
        def get_num(n):
            res=[]
            while n:
                res.append(n%10)
                n=int(n/10)
            return res
        
        visit=set([n])
        
        while True:
            n=sum(map(square,get_num(n)))
            if n==1:
                return True
            else:
                if n not in visit:
                    visit.add(n)
                else:
                    return False
```