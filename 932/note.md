## using the way of divide&conquer
这道题我们可以换个思路考虑，如果一个数的左边都是奇数，右边都是偶数，那这个数肯定满足题目条件。  
要学会按照条件往数组里添加元素。
```python3
class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        res=[1]
        while len(res)<=N:
            res=[2*i-1 for i in res]+[2*i for i in res]
        return [i for i in res if i<=N]
```