- 简单思路
我们用stack存储两个string。遇到非‘#’则append, 遇到‘#’则判断栈是否为空，不为空则pop。
```python
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack_s=[]
        stack_t=[]
        for char in S:
            if char!='#':
                stack_s.append(char)
            else:
                if stack_s==[]:
                    stack_s==[]
                else:
                    stack_s.pop()
                
        for char in T:
            if char!='#':
                stack_t.append(char)
            else:
                if stack_t==[]:
                    stack_t==[]
                else:
                    stack_t.pop()
        
        if stack_s==stack_t:
            return True
        else:
            return False
```