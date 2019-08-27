- 学会判断
The way I came up with is to use loop to juade whether char in S is the same with char in J. The easier way(maybe) is to change J into set and judge whether char in the S is also in J.
```python3
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count=0
        for i in J:
            for j in S:
                if i==j:
                    count+=1
        return count
```
```python3
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        J_set=set(J)
        count=0
        for s in S:
            if s in J_set:
                count+=1
        return count
```
