```python
class Solution:
    def isValid(self, s: str) -> bool:
        push=("(","{","[")
        pop=(")","}","]")
        
        stack=[]
        
        for char in s:
            if char in push:
                stack.append(char)
                print(stack)
            elif char in pop:
                if stack==[]:
                    return False
                elif pop.index(char)!=push.index(stack[-1]):
                    return False
                else:
                    stack.pop()
        if len(stack):
            return False
        return True
```