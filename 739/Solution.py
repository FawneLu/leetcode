```python
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n=len(T)
        res=[0]*n
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and T[stack[-1]]<=T[i]:
                stack.pop()
            if stack:
                res[i]=stack[-1]-i
            stack.append(i)
            
        return res
```
```python
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n=len(T)
        res=[0]*n
        stack=[]
        for i in range(n):
            while stack and T[stack[-1]]<T[i]:
                index=stack.pop()
                res[index]=i-index
            stack.append(i)
        return res
```