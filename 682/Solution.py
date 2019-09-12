```python
class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack=[]
        
        for char in ops:
            if char=='C':
                stack.pop()
            elif char=='D':
                stack.append(int(stack[-1])*2)
            elif char=='+':
                stack.append(int(stack[-1])+int(stack[-2]))
            else:
                stack.append(int(char))
        return sum(stack)
```