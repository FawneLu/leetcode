```python
class Solution:
    def decodeString(self, s: str) -> str:
        num=""
        stack=[]
        stack.append([1,""])
        for char in s:
            if char.isdigit():
                num+=char
            elif char=='[':
                stack.append([int(num),""])
                num=""
            elif char==']':
                n,s=stack.pop()
                stack[-1][1]+=n*s
            else:
                stack[-1][1]+=char
        return stack[-1][1]
```