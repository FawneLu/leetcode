```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operators=['+','-','*','/']
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            elif token=='+':
                stack[-2]=stack[-1]+stack[-2]
                stack.pop()
            elif token=='-':
                stack[-2]=stack[-2]-stack[-1]
                stack.pop()
            elif token=='*':
                stack[-2]=stack[-1]*stack[-2]
                stack.pop()
            elif token=='/':
                stack[-2]=int(stack[-2]/stack[-1])
                stack.pop()
        return stack[-1]
```