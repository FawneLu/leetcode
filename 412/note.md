- 注意if和elif
这题其实很简单，但是一定要习惯区分if和elif。如果用的是elif，那之后的语句都不会再进行操作了。
```python3
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res=[]
        for i in range(1,n+1):
            if i%3==0 and i%5!=0:
                res.append('Fizz')
            elif i%3!=0 and i%5==0:
                res.append('Buzz')
            elif i%3==0 and i%5==0:
                res.append('FizzBuzz')
            else:
                res.append(str(i))
        return res
```
