```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        remove_i=set()
        res=[]
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            if s[i]==')':
                if not stack:
                    remove_i.add(i)
                else:
                    stack.pop()
        
        remove_i = remove_i.union(set(stack))
        
        print(remove_i)
                    
        for i in range(len(s)):
            if i not in remove_i:
                res.append(s[i])
            
        return "".join(res)
```