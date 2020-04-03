class Solution:
    def calculate1(self, s: str) -> int:
        s = s+'$'
        
        def helper(stack,i):
            num=0
            pre_op = '+'
            
            while i<len(s):
                c=s[i]
                
                if c == ' ':
                    i+=1
                    continue

                if c.isdigit():
                    num = num*10 + int(c)
                    i+=1

                elif c == '(':
                    num,i = helper([],i+1)
                    
                else:
                    if pre_op == '+':
                        stack.append(num)

                    if pre_op == '-':
                        stack.append(-num)
                    
                    num=0
                    i+=1
                    
                    if c == ')':
                        return sum(stack),i
                    
                    pre_op=c
            
            return sum(stack)
        
        return helper([],0)

class Solution:
    def calculate1(self, s: str) -> int:
        res, num, sign, stack=0, 0, 1, [1]
        
        for i in s + "+":
            if i.isdigit():
                num = num*10+int(i)
            elif i in "+-":
                res += num*sign*stack[-1]
                sign = 1 if i=="+" else -1
                num = 0
            elif i == "(":
                stack.append(stack[-1]*sign)
                sign = 1
            elif i == ")":
                res += num*sign*stack[-1]
                num=0
                stack.pop()
        
        return res


class Solution:
    def calculate(self, s: str) -> int:
        res, num, sign = 0, 0, 1
        stack=[]
        
        for i in s:
            
            if i.isdigit():
                num = num*10+int(i)
            
            elif i in "+-":
                res += num*sign
                num = 0
                sign = 1 if i == "+" else -1
            
            elif i == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign=1
            
            elif i == ")":
                res += sign*num
                res *= stack.pop()
                res += stack.pop()
                num=0
        
        res += num*sign
        
        return res