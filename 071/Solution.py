```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        dirs=path.split('/')
        print(dirs)
        for d in dirs:
            if not d or d=='.':
                continue
            if d=='..':
                if stack:
                    stack.pop()
            else:
                stack.append(d)
        
        return '/' + '/'.join(stack)
```