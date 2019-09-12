- stack
对于stack，在python中，我们可以简单地用list表示。append表示入栈，pop表示出栈，这样也符合先进后出的原则。
这道题，遇到左边的符号我们就选择入栈，遇到右边的符号，如果对应左边的符号此时在栈的最后一位，我们就出栈，否则不满足条件。最后判断栈是否为空。栈为空，return True，否则return False。
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